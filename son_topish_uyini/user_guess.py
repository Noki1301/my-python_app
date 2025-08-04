import random 

def son_top(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>> "))
        if taxmin < tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling.")
        elif taxmin > tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling.")
        else:
            print(f"Tabriklayman! {taxminlar} ta urinishda topdingiz.")
            break
    return taxminlar

def son_top_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing!")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Sizning soningiz {taxmin} bo‘lsa (t), kattaroq bo‘lsa (+), kichikroq bo‘lsa (-): ").lower()
        if javob == '-':
            yuqori = taxmin - 1
        elif javob == '+':
            quyi = taxmin + 1
        elif javob == 't':
            print(f"Men {taxminlar} ta taxmin bilan topdim!")
            break
    return taxminlar

def play(x=10):
    while True:
        print("\n--- Foydalanuvchi topadi ---")
        taxminlar_user = son_top(x)
        print("\n--- Kompyuter topadi ---")
        taxminlar_pc = son_top_pc(x)
        
        if taxminlar_user < taxminlar_pc:
            print("Siz yutdingiz!")
        elif taxminlar_user > taxminlar_pc:
            print("Men yutdim!")
        else:
            print("Durrang!")

        yana = input("Yana o'ynaysizmi? (ha/yo'q): ").lower()
        if yana != 'ha':
            print("Xayr!")
            break

play(10)
