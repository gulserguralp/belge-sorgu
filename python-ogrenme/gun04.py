# DOSYAYA YAZMA
with open("deneme.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Birinci satir\n")
    dosya.write("Ikinci satir\n")
    dosya.write("Ucuncu satir\n")

print("yazildi")


# DOSYAYI KOMPLE OKUMA
with open("deneme.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()

print(icerik)
print(type(icerik))


# SATIR SATIR OKUMA
with open("deneme.txt", "r", encoding="utf-8") as dosya:
    satirlar = dosya.readlines()

print(satirlar)
print(len(satirlar))