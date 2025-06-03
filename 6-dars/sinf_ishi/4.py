file = None
try:
    file = open("fayl1.txt", "r")
except FileNotFoundError:
    print("Fayl topilmadi")
finally:
    if file:
        file.close()
