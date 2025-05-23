son = int(input("Son kiriting: "))
boluvchilar_yigindisi = sum(i for i in range(1, son) if son % i == 0)

if boluvchilar_yigindisi == son:
    print("Mukammal son")
else:
    print("Mukammal son emas")
