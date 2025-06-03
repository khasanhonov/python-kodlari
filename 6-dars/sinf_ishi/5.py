file = None
try:
    file = open("fayl1.txt", "w")

    for i in range(1, 101):
        file.write(f"{i}\n")
    


except FileNotFoundError:
    print("Fayl topilmadi")
finally:
    if file:
        file.close()
