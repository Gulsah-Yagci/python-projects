class Karakter():
    def __init__(self,can,guc):
        self.can = can
        self.guc = guc

    def saldir(self,rakip):
        rakip.can -= self.guc


x = Karakter(70,40)
y = Karakter(100,50)

print("birinci durum: ",x.can)
y.saldir(x)
print("ikinci durum: ",x.can)



