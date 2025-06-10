import random

with open("numbers.txt", "w") as f:
    sonlar = [str(random.randint(1, 100)) for _ in range(10)]
    f.write(" ".join(sonlar))
