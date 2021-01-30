class Kitap:
    def __init__(self,yazar,isim,sayfa):
        self.__yazar = yazar
        self.__isim = isim
        self.__sayfa = sayfa

    def getYazar(self):
        return self.__yazar

    def getIsım(self):
        return self.__isim
    def getSayfa(self):
        return self.__sayfa

    def __del__(self):
        print("{} yazarına ait {} kitabı silindi".format(self.__yazar,self.__isim))


x = Kitap()
del x
