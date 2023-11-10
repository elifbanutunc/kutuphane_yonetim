# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:42:27 2023

@author: TUNC
"""
#üyeler üzerinde ne gibi işlemler yapılabilir

def uyeEkle(uye_no,uye_ad,uye_soyad,uye_tel,uye_eposta, uye_adres):  
    
    print("Üye No:",  uye_no)
    print("Üye Ad:",  uye_ad)
    print("Üye Soyad:", uye_soyad)
    print("ÜyeTelefon:", uye_tel)
    print("Üye E-posta:", uye_eposta)
    print("Üye Adres:", uye_adres)
   
uyeEkle("2022801467", "Elif Banu", "Tunç", "5070423128", 
"elifbanutunc@gmail.com", "Kuruçeşme Mahallesi, İzmir")


def uyeSil(uye_no):
 uyeSil()
    
def uyeGuncelle(uye_no, uye_tel, uye_adres,uye_eposta):
    print( "Üye No:", uye_no)
    print("yeni telefon:", uye_tel)
    print("yeni adres:", uye_adres)
    print("yeni e-posta:", uye_eposta)
    
uyeGuncelle("00001","05076543212","Oğuzlar Mahallesi Ankara","eliftunc@gmail.com")

