class nuqta:
    def init(self, birbalo, yy):
        self.birbalo = birbalo
        self.yy = yy

    def malumot(self):
        if self.birbalo > 0 and self.yy > 0:
            return 1
        elif self.birbalo < 0 and self.yy > 0:
            return 2
        elif self.birbalo < 0 and self.yy < 0:
            return 3
        elif self.birbalo > 0 and self.yy < 0:
            return 4
        elif self.birbalo == 0 and self.yy == 0:
            return 0  
        else:
            return 1
nuqta = nuqta(-3, 5)
print(nuqta.malumot())  