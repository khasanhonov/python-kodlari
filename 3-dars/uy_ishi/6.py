n = int(input("Son kiriting: "))
yigindi = 0

for i in range(1, n+1):
    yigindi = yigindi + i
    matn = ""
    for j in range(1, i+1):
        if j == 1:
            matn = "1"
        else:
            matn = matn + "+" + str(j)
    print(matn, "=", yigindi)
