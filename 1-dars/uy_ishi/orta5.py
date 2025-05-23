N = int(input("Boshlanish N: "))
M = int(input("Tugash M: "))
K = int(input("Nechta Fibonacci soni kerak: "))

a = 0
b = 1
sana = 0

while sana < K:
    if N >= a <= M:
        print(a)
        sana += 1
    c = a + b
    a = b
    b = c
