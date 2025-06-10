with open("countries.txt") as f:
    countries = f.read().split()

with open("capitls.txt") as f:
    capitls = f.read().split()

with open("fayld.txt", "w") as f:
    for country, capital in zip(countries, capitls):
        f.write(f"{country} - {capital}\n")
