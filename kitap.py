# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 17:57:45 2023

@author: TUNC
"""

#kategori,yazar,yayınevi

def kitapEkle(kitap_barkod, kitap_ad,kategori_no, kategori_ad, yayinevi_id, yayinevi_ad, yazar_ad,adet):
    print("Kitap Barkod:", kitap_barkod)
    print("Kitap Adı:", kitap_ad)
    print("Kategori No:", kategori_no)
    print("Kategori:", kategori_ad)
    print("Yayıncılık:", yayinevi_id)
    print("Yayıncılık:", yayinevi_ad)
    print("Yazar Ad:", yazar_ad)
    print("Adet:",adet)
    
kitapEkle("351135", "Anna Karenina","9991", "Dünya Klasikleri", "23323","Deniz Yayıncılık", "Tolstoy", 100)


def kitapSil(kitap_barkod):
    kitapSil()
    
def kitapGuncelle(yayincilik_ad,adet):
    kitapGuncelle()