import csv
import datetime
import string
import pandas as pd
import xlsxwriter
a=0
for a in range(a,20987,1):
 file= open("pizzasecim.txt","r",encoding="utf-8")
 dosya=file.read()
 file.close()
 class Pizza:
             def __init__(self,aciklama,fiyat):
                         self.aciklama=aciklama
                         self.fiyat=fiyat
 Klasik=Pizza("Klasik Pizza: tüm malzemeler", 45)
 Margarita=Pizza(" Margarita Pizza: domates,kasar", 40)
 TürkPizza=Pizza(" TürkPizza:sucuk,salam,sosis", 30)
 SadePizza=Pizza(" Sade Pizza: Sucuk,kasar",35)
 class Sos:
           def __init__(self,sosfiyat):
             self.sosfiyat=sosfiyat
 Zeytin=Sos(2)
 Mantar=Sos(4)
 KeçiPeyniri=Sos(5)
 Et=Sos(7)
 Soğan=Sos(3)
 Mısır=Sos(2)
 print(dosya)
 Secim1=input("Lütfen pizza seçiniz: ")

 if (Secim1==("Klasik Pizza")):

               PizzaFiyat=Klasik.fiyat

               print(Klasik.aciklama, Klasik.fiyat)
 elif (Secim1==("Margarita Pizza")):
              PizzaFiyat=Margarita.fiyat
              print(Margarita.aciklama, Margarita.fiyat)
 elif (Secim1==("Türk Pizza")):
             PizzaFiyat=TürkPizza.fiyat
             print(TürkPizza.aciklama, TürkPizza.fiyat)
 elif (Secim1==("Sade Pizza")):
             PizzaFiyat=SadePizza.fiyat

             print(SadePizza.aciklama, SadePizza.fiyat)
 else:
              print("Menüde olmayan bir pizza seçtiniz.")

 Secim2=input("Lütfen sos seçiniz:")
 if Secim2==("Zeytin"):
             SosFiyat=Zeytin.sosfiyat
             print(SosFiyat)
 elif Secim2==("Mantar"):
             SosFiyat=Mantar.sosfiyat
             print(SosFiyat)
 elif Secim2==("Keçi Peyniri"):
             SosFiyat=KeçiPeyniri.sosfiyat
             print(SosFiyat)
 elif Secim2==("Et"):
             SosFiyat=Et.sosfiyat
             print(SosFiyat)
 elif Secim2==("Soğan"):
             SosFiyat=Soğan.sosfiyat
             print(SosFiyat)
 elif Secim2==("Mısır"):
             SosFiyat=Mısır.sosfiyat
             print(SosFiyat)
 else:
             print("Hatalı sos girdiniz.")

 Tutar=PizzaFiyat+SosFiyat
 print(f' Ödenecek tutar:{Tutar} TL')
 x=input("Adınızı ve soyadınızı giriniz:")
 y =int(input("TC kimlik no giriniz:"))
 z=int(input("Kredi kartı numaranızı giriniz:"))
 t=int(input("Kredi kart sifrenizi giriniz:"))
 kullanici={x,y,z,t,Tutar}


 
 data = {'Ad Soyad' ,'TC', 'Kredi kartı no', 'Sifre' , 'Tutar'}
 i=iter(data)
 with open('projedeneme.csv', 'a', encoding='utf-8',newline='\n') as f:
    writer = csv.writer(f)
    writer.writerow({'Ad Soyad': x })
    f.write(x)
    writer.writerow(' ')
    writer.writerow({'TC':y})
    f.write(str(y))
    writer.writerow(' ')
    writer.writerow({'Kredi kart no':z})
    f.write(str(z))
    writer.writerow(' ')
    writer.writerow({'sifre':t})
    f.write(str(t))
    writer.writerow(' ')
    writer.writerow({'Tutar':Tutar})
    f.write(str(Tutar))
    
    

