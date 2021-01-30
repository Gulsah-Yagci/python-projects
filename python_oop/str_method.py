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

    # print edildiğindeki görüntülenecek
    def __str__(self):
        return self.__yazar + " "+self.__isim+" "+str(self.__sayfa)

x = Kitap('abc','xyz',34)
print(x)