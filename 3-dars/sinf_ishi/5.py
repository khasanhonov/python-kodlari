sonlar = [5, 3, 8, 6, 7, 2]

for j in range(0, len(sonlar) - 1):
    for i in range(0, len(sonlar) - 1 - j):
        if sonlar[i] > sonlar[i+1]:
            sonlar[i], sonlar[i+1] = sonlar[i+1], sonlar[i]

print(sonlar)

