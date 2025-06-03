while True:
    try:
        son = int(input("Istalgan sonni kiriting: "))
        print("100 / son =", 100 / son)
        break
    except ValueError:
        print("Xato. Son kiriting")
    except ZeroDivisionError:
        print("Sonni 0 ga bo'lish mumkin emas")
    except:        
        print("Xato")
    finally:
        print("Tugadi")
