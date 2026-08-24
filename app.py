import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer, util
from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


@st.cache_resource
def model_yukle():
     return SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

model = model_yukle()

@st.cache_data
def belgeyi_hazirla(dosya):
    reader = PdfReader(dosya)
    tum_metin = ""
    for sayfa in reader.pages:
        tum_metin = tum_metin + sayfa.extract_text()
    cumleler = tum_metin.split(".")
    parcalar = []
    gecici = ""
    for cumle in cumleler:
        cumle = cumle.strip()
        if cumle == "":
            continue
        gecici = gecici + cumle + ". "
        if len(gecici.split()) >= 40:
            parcalar.append(gecici.strip())
            gecici = ""
    if gecici.strip() != "":
        parcalar.append(gecici.strip())
    embeddingler = model.encode(parcalar)
    return parcalar, embeddingler



st.title("Belge Sorgu Sistemi")
st.write("PDF belgesine soru sor, yapay zeka cevaplasin.")
yuklenen = st.file_uploader("PDF yukleyin", type="pdf")

if yuklenen is not None:
    parcalar, parca_embeddingleri = belgeyi_hazirla(yuklenen)
else:
    st.info("Baslamak icin bir PDF yukleyin.")
    st.stop()



soru = st.text_input("Sorunuz:")

if st.button("Sor"):
    soru_embeddingi = model.encode(soru)
    skorlu_parcalar = []
    for i in range(len(parcalar)):
        skor = util.cos_sim(soru_embeddingi, parca_embeddingleri[i]).item()
        skorlu_parcalar.append((skor, parcalar[i]))

    skorlu_parcalar.sort(reverse=True)
    en_iyi_uc = skorlu_parcalar[:3]

    baglamlar = ""
    for skor, parca in en_iyi_uc:
        baglamlar = baglamlar + parca + "\n\n"

    mesaj = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=[{"role": "user", "content": f"Asagidaki metne dayanarak soruyu cevapla. Sadece metindeki bilgiyi kullan.\n\nMetin: {baglamlar}\n\nSoru: {soru}"}]
    )

    st.subheader("Cevap:")
    st.write(mesaj.content[0].text)
    st.caption("Kaynak parcalar:")
    for skor, parca in en_iyi_uc:
        st.text(f"(skor: {skor:.2f})")
        st.text(parca)