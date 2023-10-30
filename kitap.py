# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 17:57:45 2023

@author: TUNC
"""

#kategori,yazar,yayınevi

def kitapEkle(kitap_barkod, kitap_ad,kategori_no, kategori_ad, yayinevi_id, yayinevi_ad, yazar_ID, yazar_ad,adet):
    print("Kitap Barkod:", kitap_barkod)
    print("Kitap Adı:", kitap_ad)
    print("Kategori No:", kategori_no)
    print("Kategori:", kategori_ad)
    print("Yayıncılık:", yayinevi_id)
    print("Yayıncılık:", yayinevi_ad)
    print("Yazar Ad:", yazar_ad)
    print("Adet:",adet)
    
kitapEkle("3511350", "Anna Karenina","001", "Roman", "23323","Deniz Yayıncılık", "193838000", "Tolstoy", 100)


def kitapSil(kitap_barkod):
    kitapSil()
    
def kitapGuncelle(yayincilik_ad,adet):
    kitapGuncelle()