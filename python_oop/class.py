class Insan():
    isim = "ali"
    guc = 55

# bu sekilde isime ve guce erişim verir

class Insan2():
    # yapıcı method
    def __init__(self,name,guc): # name ve guc dışarıdan atanacak
        self.name = name
        self.damage = guc # self'i farklı adlandırabilirsin
    # self ile bu yukarıdaki değişkenlerin classa ait olduğu belirtilir.
    def setName(self,isim):
        self.name = isim
    # set/get işlemlerini kapsülleme yapılmalı
oyuncu = Insan2('ali',44)

print(oyuncu.name)
print(oyuncu.setName('mehmet'))
