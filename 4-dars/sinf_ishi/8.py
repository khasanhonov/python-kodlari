
login = {
    "jeymsBond": "agent007",
    "tony_stark": "ironman101",
    "piterParker": "spider.12.12",
    "sherlok": "sher.l04",
}

l = "sherlok"
p = "sher.l04"

for log, par in login.items():
    if log == l and par == p:
        print(f"Siz kirdingiz 😏")
        break
else:    
    print("Yoqole")

 