# satr = input("Sonlarni kiriting: ")
# son = input("Qidiriladigan son:")
# if son in satr:
#     print("Ha bor")
# else:
#     print("Yo'q")

sonlar = input("Sonlarni kiriting: ").split(" ")
print(sonlar)
for i in range(0, len(sonlar)):
     sonlar[i] = int(sonlar[i])
    
print(sonlar)
