import json

i = 0
with open("hodimlar.json", "r") as file:
    odamlar = json.load(file)
    for odam in odamlar:
        if odam['is_student']:
            print(f"{odam['name']} {odam['age']} {odam['education']['university']}")
