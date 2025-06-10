try:
    a = int(input("Birinchi son: "))
    b = int(input("Ikkinchi son: "))
    print(a, b)
except ValueError:
    print("Raqam kiriting")
except ZeroDivisionError:
    print("Sonni 0 ga bolish mumin emas")
