#liste
meyveler= ["elma", "armut","kiraz"]

print(meyveler)
print(meyveler[0])   #ilk eleman
print(meyveler[-1]) #son eleman
print(len(meyveler)) #uzunluk

meyveler.append("muz") #sona ekle
print(meyveler)


meyveler.remove("armut") #değere göre sil
print(meyveler)

#DİLİMLE (slicing)

sayilar = [10, 20, 30, 40, 50]
print(sayilar [1:3]) # 1 den 3 e kadar, 3 dahil değil
print (sayilar[:2]) # baştan 2 ye
print (sayilar[2:]) # 2 den sonra   


#SÖZLÜK 
ogrenci = {
    "ad": "Gülser",
    "bolum": "Bişgisayar Mühendisliği",
    "sinif": 4

}


print(ogrenci)
print(ogrenci["ad"])
print(ogrenci["sinif"])


ogrenci["universite"] = "NİŞANTAŞI ÜNİVERSİTESİ"  #yeni anahtar ekle
print(ogrenci)

#güvenli erişim
print(ogrenci.get("not_ortalaması"))  #none döner,hata vermesz
print(ogrenci.get("not_ortalaması", "yok"))  #varssayılan değer

#bu hata verir
#print(ogrenci["not_ortalaması"])

for anahtar in ogrenci:
    print(anahtar, "->", ogrenci[anahtar])