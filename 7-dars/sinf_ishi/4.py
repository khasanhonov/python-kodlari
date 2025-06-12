class HisobRaqami:

    def __init__(self, ism, balans):
        self.ism = ism
        self.balans = balans
        # atribut
        # metod

    def ekranga(self):
        print(f"{self.ism} {self.balans}")

def test():
    pass



anvar = HisobRaqami("Anvar", 1_000_000)

anvar.ekranga()

otabek = HisobRaqami("Otabek", 2_000_000)

otabek.ekranga()
