"""""

#Veri Tipler ive String İşlemleri
    # Girilen iki değerin ort alma örneği

isim=input("Adınızı giriniz:")
vize=int(input("İlk Notunuzu Giriniz: "))
final=int(input("İkinci Notunuzu Giriniz: "))

#ortalama=(int(vize)+int(final))/2
ortalama=(vize+final)/2
print(ortalama)


## Loops ~ decision structures
sinif=int(input("Kaç not ortalanacak? "))

while sinif<0:
    isim=input("Öğrenci adı: ")
    vize=int(input("Vize notu:"))
    Final=int(input("Final notu:"))

    ortalama=(vize+final)/2
    print(ortalama)

    sinif=-1

#while if mantığı

x=1
while True:
    print(x)
    x=+1
    if x!=x:
        break #şart sağlandığı sürece çalışacakrtır


#Hafızda tutulan rastgele değeri çıkarma
import random
rnd=random.randint(1,100)
tries=0

while True:
    guess=int(input("Find the Number!"))
    tries+=1
    if guess==rnd:
        print("You found it")
        #break
    elif rnd>guess:
        print("Try big one!")
    else: print("Whoza, take small one...")

"""""

"""""

#iki veya daha fazla tür ile range değerleri arasında değer tablosu elde etme. en temeli ile:
for a in range(1,10):
    for b in range(10,100,10):
     print("a={} -  b={}" .format(a,b))
     print("-------------")

"""""


#json ile veri okuma

import requests
adress="https://finans.truncgil.com/today.json"

statue=requests.get(adress) #var mu diye bakıyoruz
datasample=statue.json()

print(datasample)

##

tarih=datasample["Update_Date"]
gbp=datasample["GBP"]
alis=gbp["Alış"]
satis=gbp["Satış"]
message="Günaydın, {} tarihine ait GBP kur bilgileri şöyledir: \n Alış Bilgileri:{} \n Satış Bilgileri:{} \n İyi Günler..." .format(tarih,alis,satis)
print(message)

#json dosyasında "deneme1": -----> şeklindeki tanımlara key denir. bir keyin birden fazla value değeri olabilir. 
    #"deneme1"[{values_1}, {values_2}, {values_3} ] ... "deneme8"[{values_1}, {values_2} ] şeklinde olabilir.
    # her value da tıpkı bir key gibi tanımlanır örnek: "deneme1"[ {"value1" : "123", "value2" : "abc"} .... ]


import requests
adres="https://pomber.github.io/covid19/timeseries.json"
veri=requests.get(adres).json() # aldığım gibi get işlemi yaptım bu sefer

tr=veri["Turkey"]
print(tr)

sonGün=tr[-1]
sonVaka=sonGün["date"]
a=sonGün["confirmed"]
b=sonGün["deaths"]
c=sonGün["recovered"]