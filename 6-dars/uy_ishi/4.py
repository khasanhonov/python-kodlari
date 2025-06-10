try:
    soat = float(input("Ishlangan soatlarni kiriting: "))
    stavka = float(input("Soatlik maoshingizni kiriting: "))

    if soat > 40:
        tolov=40*stavka+(soat - 40) * stavka * 1.5
    else:
        tolov = soat * stavka

    print("To'lov:", tolov)
except ValueError:
    print("Xato, iltimos, raqam kiriting")
