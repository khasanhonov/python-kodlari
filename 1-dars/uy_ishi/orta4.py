N = int(input("N ni kiriting: "))
a, b = 0, 1
for _ in range(N):
    print(a)
    a, b = b, a + b
