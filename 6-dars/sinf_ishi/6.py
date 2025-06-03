file = None
try:
    file = open("fayl2.txt", "a")
    royxat = [Otabek, Ulugkbek]
    javob = list(map(str, royxat))
    
    file.write("+".join(javob))
    


except FileNotFoundError:
    print("Fayl topilmadi")
finally:
    if file:
        file.close()
