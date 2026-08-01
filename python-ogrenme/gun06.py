from pypdf import PdfReader

#pdf i oku tek metinde birleştit

reader = PdfReader("test.pdf")

tum_metin=""
for sayfa in reader.pages:
    tum_metin = tum_metin + sayfa.extract_text()

print("Toplam Karakter:", len(tum_metin))


#metni kelimelere ayır

kelimeler = tum_metin.split()
print("Toplam Kelime: ", len(kelimeler))

#her parça 50 kelime olacak şekilde böl

parca_boyutu= 100
parcalar =[]

for i in range(0,len(kelimeler), parca_boyutu):
    parca_kelimeleri=kelimeler[i:i + parca_boyutu]
    parca=" ".join(parca_kelimeleri)
    parcalar.append(parca)

print("parca sayisi:", len(parcalar))
print("---İLK PARÇA---")
print(parcalar[0])