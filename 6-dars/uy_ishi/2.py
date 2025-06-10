
try:
    lst = list(map(int, input("Sonlar: ").split()))
    indeks = int(input("Indeks: "))
    print(lst[indeks])
except IndexError:
    print("Bunday indeks mavjud emas")
