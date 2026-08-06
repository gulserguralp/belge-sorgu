from pypdf import PdfReader
from sentence_transformers import SentenceTransformer, util

# ---- 1. adım pdf i okun gün05 ----
reader = PdfReader("test.pdf")
tum_metin= ""
for sayfa in reader.pages:
    tum_metin = tum_metin + sayfa.extract_text()

# ---- 2. adım parçalara böl gün06 ---
kelimeler= tum_metin.split()
parca_boyutu= 40
parcalar=[]
for i in range(0, len(kelimeler), parca_boyutu):
    parca= " ".join(kelimeler[i:i+parca_boyutu])
    parcalar.append(parca)

print("Parca sayisi: ", len(parcalar))

# ---- 3. adım her parçayı embedding e çevir gün07---
model= SentenceTransformer("all-MiniLM-L6-v2")
parca_embeddingleri= model.encode(parcalar)

#---- 4. adım kullanıcının sorusu ---
soru= "Öfke hangi organla ilişkili?"
soru_embeddingi= model.encode(soru)

#----- 5. adım Soruyu her parcayla karsilastir, en yakini bul ---
en_yuksek_skor= -1
en_iyi_parca=""

for i in range(len(parcalar)):
    skor= util.cos_sim(soru_embeddingi, parca_embeddingleri[i]).item()
    if skor>en_yuksek_skor:
        en_yuksek_skor=skor
        en_iyi_parca=parcalar[i]


print("---SORU---")
print(soru)
print("--- EN ILGILI PARCA (skor:", en_yuksek_skor, ") ---")
print(en_iyi_parca)