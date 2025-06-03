file = None
try:
    file = open("fayl1.txt", "w")
    royxat = [1,3,4,5,6]
    javob = list(map(str, royxat))
    
    file.write("+".join(javob))
    


except FileNotFoundError:
    print("Fayl topilmadi")
finally:
    if file:
        file.close()
