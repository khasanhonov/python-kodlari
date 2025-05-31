# meva = input("Bozordan qaysi mevani qidiryapsiz: ")
# bozor = {
#     "olma": 5000,
#     "nok": 5_000,
#     "banan": 20_000,
#     "anor": 10_000
# }

# qo'shish
# print(bozor)
# bozor["qulupnay"] = 50_000
# print(bozor)
# bozor.update({"tut":10_000, "shaftoli": 20_000})
# print(bozor)

# kalitlari
# print(list(bozor.keys()))
# for key in bozor.keys():
    # print(key)

# qiymatlari
# for val in bozor.values():
    # print(val)

# ikkalasi
# for key in bozor.keys():
#     print(key, bozor[key])

# YOKI

# for meva, narxi  in bozor.items():
#     print(f"{meva}:{narxi}")

# print(list(bozor.items()))
# a,b = 20,40
# a,b,c = (20,40,30)
# print(a,b)

# print("bodring" in bozor.keys())
# print(5000 in bozor.values())

# for meva, narxi in bozor.items():
#     if 50_000 > narxi > 5000:
#         print(meva)


# bozor = {
#     "olma": 5000,
#     "nok": 5_000,
#     "banan": 20_000,
#     "anor": 10_000
# }
# o'chirish
# bozor.popitem()
# bozor.pop("olma")
# del bozor["anor"]
# del bozor
# bozor.clear()
# print(bozor)

bozor = {
    "olma": {"xitoy": 5000, "vodiy": 20000},
    "nok": {"xitoy": 5000, "vodiy": 20000},
    "banan": {"xitoy": 5000, "vodiy": 20000},
    "anor": {"xitoy": 5000, "vodiy": 20000}
}

royxat = ["olma", "nok", "o'rik"]
summa = 0
for mahsulot in royxat:
    if mahsulot in bozor:
        summa += bozor[mahsulot]["vodiy"]
    else:
        print(f"{mahsulot} bozorda yo'q")
print(f"Hammasi {summa} so'm")
