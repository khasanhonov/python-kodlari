N = int(input("N ni kiriting: "))
M = int(input("M ni kiriting: "))
K = int(input("K ni kiriting: "))

j = 0      
yigindi = 0   

for i in range(N, M + 1):
    if i % 2 == 0:
        yigindi += i
        j += 1
        if j == K:
            break

print("Yig'indi:", yigindi)
