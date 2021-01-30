class Dusman():
    def __init__(self):
        self.can = 100
        self.guc = 40

    def saldır(self,oyuncu):
        oyuncu.can -= self.guc


class Oyuncu():
    def __init__(self):
        self.can = 500
        self.can = 100

    def saldır(self,dusman):
        dusman.can -=self.guc



player = Oyuncu()

dusmanlar = []

for i in range(10):
    dusmanlar.append(Dusman())

dusmanlar[0].can
player.vur(dusmanlar[3])

