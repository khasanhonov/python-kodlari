import json

i = 0
skill = input("Malakani kiriting: ")
with open("hodimlar.json", "r") as file:
    odamlar = json.load(file)
    print("_" * 70)
    print()
    print(f"|{'Ism familiya'.center(30)} | {'Yosh'.center(5)} | {'Universitet'.center(30)}|")
    print("_" * 70)
    for odam in odamlar:
        for skill_ in odam['skills']:            
            if skill in skill_:
                print(f"|{odam['name'].center(30)} | {str(odam['age']).center(5)} | {skill_.center(30)}|")
                break
