class vaxt:
    def init(self, soat, minutlar, sikundlar):
        self.soat = soat
        self.minutlar = minutlar
        self.sikundlar = sikundlar

    def vaxt_left(self):
        total_now = self.soat * 60 + self.minutlar + self.sikundlar / 60
        total_24h = 24 * 60
        return int(total_24h - total_now)

    def add_minutlars(self, minutlars):
        aaa = self.soat * 3600 + self.minutlar * 60 + self.sikundlar
        aaa += minutlars * 60

        h = (aaa // 3600) % 24
        m = (aaa % 3600) // 60
        s = aaa % 60

        return f"{int(h):02d}:{int(m):02d}:{int(s):02d}"

    def str(self):
        return f"{self.soat:02d}:{self.minutlar:02d}:{self.sikundlar:02d}"

vaxt1 = vaxt(21, 15, 30)
vaxt2 = vaxt(22, 45, 0)
vaxt3 = vaxt(13, 0, 0)
vaxt4 = vaxt(23, 59, 59)
vaxt5 = vaxt(0, 0, 0)

obeyekt = [vaxt1, vaxt2, vaxt3, vaxt4, vaxt5]

for t in obeyekt:
    print("Vaqt:", t)
    print("24:00:00 gacha qolgan daqiqa:", t.vaxt_left())
    print("100 daqiqa qo‘shilgandan so‘ng:", t.add_minutlars(100))
    print()