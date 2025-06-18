from users import User, user_crud

def admin_menu():
    while True:
        habar = """
    Admin panel
        1. Foydalanuvchi +
        2. Mahsulot
        3. Buyurtma    
        5. Chiqish
        """
        tanlov = 0
        while True:
            try:
                tanlov = int(input(habar))
                assert tanlov in range(1,6)
                break
            except:
                print("Xato. Qayta kiriting")
        if tanlov == 1:
            user_crud()            
        elif tanlov == 5:
            return

    


def user_menu():
    habar = """
    Amallardan birini tanlang:
        1. Mahsulotni ko'rish
        2. Mahsulot qidirish
        3. Mahsulotni filtrlash            
        4. Savatchaga qo'shish olish
        5. Savatchani ko'rish (Har biri va Jami mahsulot summasi)
        6. Savatchadan o'chirish
        7. Profil
        0. Chiqish
        """
    while True:
        
        tanlov = 0
        while True:
            try:
                tanlov = int(input(habar))
                assert tanlov in range(0,8)
                break
            except:
                print("Xato. Qayta kiriting")
        if tanlov == 1:
            pass
        elif tanlov == 0:
            return
def menu():
    habar = """
    Bittasini tanlang:
        1. Kirish
        2. Ro'yxatdan o'tish
        3. Chiqish
    """
    while True:
        try:
            tanlov = int(input(habar))
            assert tanlov in [1,2,3]
            return tanlov
        except:
            print("Xato. Qayta kiriting")



while True:
    tanlov = menu()

    if tanlov == 1:
        username = input("Login kiriting")
        password = input("Parolni kiriting: ")
        username, role = User.login(username, password)
        if username:
            if role == "user":
                user_menu()
            elif role == "admin":
                admin_menu()

    elif tanlov == 2:
        username = input("Login kiriting")
        password = input("Parolni kiriting: ")
        if User.create(username,password):
            print("Ro'yxatdan o'tdingiz")
    else:
        break