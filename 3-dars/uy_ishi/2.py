a = 10
b = 20
sonlar = []

for i in range(b-1, a-1, -1):
    if i % 2 != 0:
        sonlar.append(i)

print("sonlar =", sonlar)
