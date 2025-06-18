class Developer:
    def __init__(self, familiyasi, leveli, oylikdaromadi):
        self.familiyasi = familiyasi
        self.leveli = leveli
        self.oylikdaromadi = oylikdaromadi

class SoftwareEngineer(Developer):
    def __init__(self, familiyasi, leveli, oylikdaromadi, bonus, department):
        super().__init__(familiyasi, leveli, oylikdaromadi)
        self.bonus = bonus
        self.department = department

    def total_oylikdaromadi(self):
        return self.oylikdaromadi + self.bonus

    def developers(self)
    for dept, info in result.items():
        print(f"{dept}: {self.developers['count']} ta dasturchi, jami tolov: {self.developers['total']}")


a = SoftwareEngineer("Anvar", "Junior", 500, 100, "1-bolim")
b = SoftwareEngineer("Asror", "Middle", 1500, 500, "2-bolim")
c = SoftwareEngineer("Kamola", "Senior", 2500, 100, "3-bolim")
d = SoftwareEngineer("Vali", "Junior", 500, 100, "1-bolim")
e = SoftwareEngineer("Davron", "Middle", 1500, 100, "2-bolim")
developers = [a, b, c, d, e]


