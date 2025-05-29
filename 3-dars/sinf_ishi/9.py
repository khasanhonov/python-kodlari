
nechta = int(input("Nechta son kiritasiz: "))

sonlar = []
sonlar.insert(0,3)
sonlar.insert(0,6)
for i in range(0, nechta):
    son = int(input(f"{i+1} sonni kiriting: "))
    sonlar.append(son)
print(sonlar)
