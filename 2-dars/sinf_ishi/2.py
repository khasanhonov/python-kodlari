n = int(input("n ni kiriting: "))
k = 0
while 3 ** (k + 1) <= n:
    k += 1
print("Natija:", k)
