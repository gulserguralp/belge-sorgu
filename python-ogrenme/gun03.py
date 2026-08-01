sayilar = [12,7,45,3,28]
#koşul - parantez yok, iki nokta var, girinti şart
for sayi in sayilar:
    if sayi > 20:
        print(f"{sayi} buyuk")

    elif sayi> 10:
        print(f"{sayi} orta")

    else:
        print(f"{sayi} küçük")



#range ile sayarak dönme

for i in range(5):
    print(i) #0 dan 4 e kadar, 5 dahil değil

#enumarate - hem sirayi hem değeri verir

meyveler= ["elma", "armut", "kiraz"]

for sira, meyve in enumerate(meyveler):
    print(sira,meyve)



#while- koşul sağlandığı sürece
sayac= 0
while sayac < 3:
    print("sayac:", sayac)
    sayac= sayac + 1

#LİST COMPREHENSION
sayilar=[1,2,3,4,5]

#uzun yol
kareler= []
for s in sayilar:
    kareler.append(s*s)
print(kareler)

#kısa yol
kareler2= [s * s for s in sayilar]
print(kareler2)

#filtreli
ciftler= [s for s in sayilar if s % 2 ==0]
print(ciftler)


#fonksiyonlar

def selamla(ad):
    return f"merhaba {ad}"
print(selamla("gulser"))

def topla(a,b):
    return a+b
print(topla(3,5))

#varsayılan değer
def selamla2(ad, mesaj="merhaba"):
    return f"{mesaj} {ad}"

print(selamla2("gulser"))
print(selamla2("gulser", " günaydın"))

#return olmazsa none döner
def yazdir(ad):
    print(ad)

sonuc= yazdir("test")
print(sonuc)


    