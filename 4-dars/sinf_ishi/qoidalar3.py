meva = input("Bozordan qaysi mevani qidiryapsiz: ")
bozor = {
    "olma": 5000,
    "nok": 10_000,
    "banan": 20_000,
    "anor": 10_000
}
# print(f"Narxi: {bozor.get(meva)}")
# print(f"Narxi: {bozor[meva]}")
if meva in bozor:
    print(f"Narxi: {bozor[meva]}")
