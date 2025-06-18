class Dorixona:
    
    def __init__(self, nomi: str, manzili: str) -> None:
        self.nomi = nomi
        self.manzil = manzili
        self.__dorilar = []
        self.balans = 0 

    def dori_kirit(self, nomi, narxi, soni):
        assert isinstance(nomi, str), "Nomi satr bo'lishi kerak"
        assert isinstance(soni, (int, float)), "Soni int yoki float bo'lishi kerak"
        
        self.__dorilar.append({"nomi": nomi, "narxi": narxi, "soni": soni})
        print(f"{soni} dona {nomi} dori qo'shildi.")

    def malumot(self):
        print("Dori xonada mavjud dari darmonlar")
        for dori in self.__dorilar:
            print(f"{dori['nomi']} - {dori['narxi']} so'm, {dori['soni']} dona")

    def narxini_yengilash(self, nomi:str, narxi:int):
        for dori in self.__dorilar:
            if dori['nomi'] == nomi:
                dori['narxi'] == narxi:
                print(f"{narxi} dori narxi yengilandi.")

    def dorini_sot(self, nomi:str, soni:int):
        for dori in self.__dorilar:
            if dori['nomi'] == nomi:
                if dori['soni'] >=soni:
                    dori['soni'] -= soni
                    jami = soni['narxi'] * soni 
                    self.__balans += jami
                    # 10 dona Paracetamol dori sotildi. Jami: 20000 so'm
                    # Hisobga 20000 so'm qo'shildi. Joriy balans: 20000 so'm
                    print(f"{soni} dona {nomi} dori sotildi. Jami: {jami} so'm")
                    print(f"Hisobga {jami} so'm qoshildi, joriy balans: {self.__balans } so'm")

                    if dori['soni'] == 0:
                        self.__dorilar.remove(dori)
                    return
                else:
                    print(f"{nomi} yetarli emas, {dori['soni']} ta qolgan.")
        print(f"{nomi} bazada yoq")


dorixona = Dorixona(nomi="Shifokor Dorixonasi", manzili="Toshkent, O'zbekiston")
dorixona.dori_kirit(nomi="Paracetamol", narxi=2000, soni=50)
dorixona.dori_kirit(nomi="Ibuprofen", narxi=3000, soni=30)
# Output: 30 dona Ibuprofen dori qo'shildi.

dorixona.malumot()

dorixona.dorini_sot()
dorixona.dorini.sot(nomi, soni)


dorixona.narxini_yengilash()



