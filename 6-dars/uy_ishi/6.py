import math
with open ("fayl.txt") as f:
    sonlar = list(map(int, f.read().split()))

ildizlar = [str(int(math.sqrt(x))) for x in sonlar]

with open("ildiz.txt", "w") as f:
    f.write(" ".join(ildizlar))
