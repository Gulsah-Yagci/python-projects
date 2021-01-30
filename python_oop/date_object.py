from datetime import date,datetime

class Kitap:
    def __init__(self,yazar,isim,basimtarihi:date,sayfasayisi): # basimtarihi:date -date olarak vermeni ister.
        self.yazar = yazar
        self.isim = isim
        self.basimtarihi = basimtarihi
        self.sayfasayisi = sayfasayisi


x = Kitap ("sada","sads",date(2018,3,5),140)
print(x) # objenin yer bilgisini verir
print(x.basimtarihi) # bunu özel bir methodla bastırır
print(x.basimtarihi.day)
