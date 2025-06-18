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
    
    def get_medicines_info(self, nomi, narxi, soni):
        self.__dorilar.append({"nomi": nomi, "narxi": narxi, "soni": soni})
        print(f"Nomi: {self.nomi}\nNarxi: {self.narxi}\nSoni: {self.soni}")

dorixona = Dorixona(nomi="Shifokor Dorixonasi", manzili="Toshkent, O'zbekiston")
dorixona.dori_kirit(nomi="Paracetamol", narxi=2000, soni=50)
dorixona.dori_kirit(nomi="Ibuprofen", narxi=3000, soni=30)
# Output: 30 dona Ibuprofen dori qo'shildi.