from pypdf import PdfReader
from sentence_transformers import SentenceTransformer, util
from anthropic import Anthropic
from dotenv import load_dotenv
import os


#anahtarı .env dosyasına yükle
load_dotenv()
client= Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

#pdf i oku ve parçalara böl
reader= PdfReader("test.pdf")
tum_metin=""
for sayfa in reader.pages:
    tum_metin = tum_metin + sayfa.extract_text()

kelimeler= tum_metin.split()
parca_boyutu= 40
parcalar=[]
for i in range(0,len(kelimeler), parca_boyutu):
    parca= "".join(kelimeler[i:i + parca_boyutu])
    parcalar.append(parca)

#embedding
model= SentenceTransformer("all-MiniLM-L6-v2")
parca_embeddingleri= model.encode(parcalar)

# --- Soru ve en ilgili parcayi bul ---
soru= "Ayurveda nedir?"
soru_embeddingi= model.encode(soru)

en_yuksek_skor = -1
en_iyi_parca = ""
for i in range(len(parcalar)):
    skor = util.cos_sim(soru_embeddingi, parca_embeddingleri[i]).item()
    if skor > en_yuksek_skor:
        en_yuksek_skor = skor
        en_iyi_parca = parcalar[i]

# --- Parcayi Claude'a ver, cevap urettir ---
mesaj = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=500,
    messages=[
        {
            "role": "user",
            "content": f"Asagidaki metne dayanarak soruyu cevapla. Sadece metindeki bilgiyi kullan.\n\nMetin: {en_iyi_parca}\n\nSoru: {soru}"
        }
    ]
)

print("--- SORU ---")
print(soru)
print("--- CLAUDE CEVABI ---")
print(mesaj.content[0].text)    