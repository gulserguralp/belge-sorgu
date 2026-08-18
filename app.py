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
    return SentenceTransformer("all-MiniLM-L6-v2")

model = model_yukle()

@st.cache_data
def belgeyi_hazirla(dosya):
    reader = PdfReader(dosya)
    tum_metin = ""
    for sayfa in reader.pages:
        tum_metin = tum_metin + sayfa.extract_text()
    kelimeler = tum_metin.split()
    parcalar = []
    for i in range(0, len(kelimeler), 40):
        parcalar.append(" ".join(kelimeler[i:i + 40]))
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
    en_yuksek_skor = -1
    en_iyi_parca = ""
    for i in range(len(parcalar)):
        skor = util.cos_sim(soru_embeddingi, parca_embeddingleri[i]).item()
        if skor > en_yuksek_skor:
            en_yuksek_skor = skor
            en_iyi_parca = parcalar[i]

    mesaj = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=[{"role": "user", "content": f"Asagidaki metne dayanarak soruyu cevapla. Sadece metindeki bilgiyi kullan.\n\nMetin: {en_iyi_parca}\n\nSoru: {soru}"}]
    )

    st.subheader("Cevap:")
    st.write(mesaj.content[0].text)
    st.caption(f"Kaynak parca (skor: {en_yuksek_skor:.2f})")
    st.text(en_iyi_parca)