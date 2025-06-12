class Moshin:
    def init(self, tezlik, vaxt):
        self.tezlik = tezlik
        self.vaxt = vaxt

    def xaqida(self):
        return self.tezlik * self.vaxt

moshin = moshin(60, 2)
print(moshin.xaqida())  