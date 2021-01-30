class Birey:
    def __init__(self,isim,soyisim):
        self.isim = isim
        self.soyisim = soyisim

class Calismayan(Birey):pass

class Calısan(Birey): # init çalışmaz zaten var miras alınmış kabul eder.
    # override edebiliriz.
    def __init__(self,isim,soyisim,id,maas):
        Birey.__init__(self,isim,soyisim)
        self.id = id
        self.maas = maas

class Muhendis(Calısan):
    def __init__(self,isim,soyisim,id,maas,diller:tuple,yazilim_dilleri:tuple):
        Calısan.__init__(self,isim,soyisim,id,maas)
        self.diller = diller
        self.yazilim_dilleri = yazilim_dilleri
class Muhasebeci(Calısan):
    def __init__(self, isim, soyisim, id, maas, diller: tuple,programlar:tuple):
        Calısan.__init__(self, isim, soyisim, id, maas)
        self.diller = diller
        self.programlar = programlar

