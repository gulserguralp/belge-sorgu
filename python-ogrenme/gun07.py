from sentence_transformers import SentenceTransformer

#modeli yükle (il çalıştırmada internetten iner,sonra cache'ten gelir)
model = SentenceTransformer("all-MiniLM-L6-v2")

cumleler = [
    "Kalp vucudun en onemli organidir",
    "Yurek saglikli beslemeyle korunur",
    "Bugun hava cok guzel"
]

embeddingler= model.encode(cumleler)

print("kac cumle: ", len(embeddingler))
print("Her embedding kac sayidan olusuyor:", len(embeddingler[0]))
print("--- ILK CUMLENİN ILK 10 SAYISI---")
print(embeddingler[0][:10])


from sentence_transformers import util

#cumleleri ikişer ikişer karşılaştır (benzerlik skoru)

skor_kalp_yurek = util.cos_sim(embeddingler[0], embeddingler[1])
skor_kalp_hava= util.cos_sim(embeddingler[0], embeddingler[2])

print("kalp-yürek benzerliği: ", skor_kalp_yurek)
print("kalp-hava benzerliği: ", skor_kalp_hava)
