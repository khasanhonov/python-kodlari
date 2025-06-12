class HisobRaqami:

    def __init__(self, ism, balans):
        self.ism = ism
        self.balans = balans

    def pul_tushir(self, pul):
        if pul < self.balans:
            pul += self.balans

    def pul_yechish(self, yechish):
        if yechish > self.balans:
            print("Balansizda mablag' yetarli emas")
        else:
            self.balans -= yechish



    def ekranga(self):
         print(f"{self.ism} {self.balans}")

anvar = HisobRaqami("Anvar", 1_000_000)

anvar.ekranga()

pul = 2_000_000
yechish = 4_000_000


