class Araba:
    def __init__(self):
        self.hiz = 0

x =Araba()
print(x.hiz)

class Araba2:
    def __init__(self):
        self.__hiz = 0 #private

    def setHiz(self,hiz):
        self.__hiz = hiz

    def getHiz(self):
        return self.__hiz
y = Araba2()

print(y.getHiz())
print(y.setHiz(34))

