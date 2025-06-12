from math import pi



class Aylana:

    def __init__(self, radius, rangi):
        self.__radius = radius
        self.__rangi = rangi

    # o'qish
    def get_radius(self):
        return self.__radius
    # yozish
    def set_radius(self, radius):
        assert isinstance(radius,(int,float)), "Qiymat int yoki float bo'lishi kerak"
        self.__radius = radius
    
        # o'qish
    def get_rangi(self):
        return self.__rangi
    # yozish
    def set_rangi(self, rangi):
        assert isinstance(rangi,str), "str bo'lishi kerak"
        self.__rangi = rangi

    def yuzini_top(self):
        return pi * self.__radius ** 2
    
    def uzunligini_top(self):
        return 2 * pi * self.__radius

    def __str__(self):
        return f"""
        Radiusi: {self.__radius} 
        Rangi: {self.__rangi} 
        Yuzi: {round(self.yuzini_top(),2)} 
        Uzunligi: {round(self.uzunligini_top(),2)}
"""
    
    

aylana1 = Aylana(10, "oq")
print(aylana1)
aylana1.set_rangi("yashil")
aylana1.set_radius(15)
print(aylana1)
