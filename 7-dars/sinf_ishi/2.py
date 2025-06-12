# royxat = [3,4,6]

# royxat1 = []

# def kirit(son):
#     royxat.append(son)

# def chiqar():
#     return royxat.pop()



# def kirit1(son):
#     royxat1.append(son)

# def chiqar1():
#     return royxat1.pop()


# royxat1 = 4
# kirit(2)
# kirit(3)
# kirit(4)
# print(chiqar())
# print(chiqar())
# print(chiqar())


class LIFO:

    def __init__(self):
        self.__royxat = []
        
    def kirit(self, son):
        self.royxat.append(son)

    def chiqar(self):
        return self.royxat.pop()
    
    def ekranga_chiqar(self):
        print(self.royxat)


royxat1 = LIFO()
royxat1.__royxat  = 10
# royxat1.kirit(1)
# royxat1.kirit(2)
# royxat1.kirit(4)

royxat2 = LIFO()
royxat2.kirit(10)
royxat2.kirit(11)
royxat2.kirit(12)
