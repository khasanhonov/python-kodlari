from math import pi



class Aylana:

    def __init__(self, radius, rangi):
        self.__radius = radius
        self.rangi = rangi

    # o'qish
    def get_radius(self):
        return self.__radius
    # yozish
    def set_radius(self, radius):
        # if isinstance(radius,(int,float)):
        #     self.__radius = radius
        # else:
        #     raise TypeError("Qiymat int yoki float bo'lishi kerak")
        assert isinstance(radius,(int,float)), "Qiymat int yoki float bo'lishi kerak"
        self.__radius = radius

    def __str__(self):
        return f"{self.__radius} {self.rangi}"
    
    

aylana1 = Aylana(10, "oq")

print(aylana1.rangi)
print(aylana1)
