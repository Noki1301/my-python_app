# print("Yaqin do'stlaringizni kiriting?")
# ismlar = []
# n=1
# while True:
#     savol = f"{n}-do'stingizni ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     n+=1
#     if takrorlash != 'ha':
#             break
# print("Do'stlaringiz ro'yxati:")
# print(*ismlar, sep="\n")

# print("Do'stalaringizning yoshini saqlaymiz:")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingizni ismini kiriting: ")
#     yosh = input(f"{ism}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)
#     takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if takrorlash == "yo'q":
#         ishora = False
# for ism, yosh in dostlar.items():
#     print(f"{ism} {yosh} yoshda")

# cars = ["nexia", "malibu", "gentra", "damas","nexia","tico","matiz","chevrolet"]

# car = "nexia"

# while car in cars:
#     cars.remove(car)
# print(cars)

# talabalar = ["ali", "vali", "hasan", "husan"]
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba}ning bahosini kiriting: ")
#     print(f"{talaba}ning bahosini kiriting: {baho}")
#     baholangan_talabalar[talaba] = int(baho)
#     print(f"{talaba}ning bahosi {baho}ga baholandi!")
# print(baholangan_talabalar)

# Amaliyot 1 masala
# print("Buyurtmalaringizni kiritadigan dastur")
# buyurtmalar = []
# n = 1
# while True:
#     buyurtma = input(f"{n}-buyurtmangizni kiriting: ")
#     buyurtmalar.append(buyurtma)  # bu yerga ko‘chirdik
#     n += 1
#     savol = input("Yana buyurtma kiritasizmi? (ha/yo'q): ")
#     if savol.lower() != 'ha':
#         break
# print("Buyurtmalaringiz:")
# print(*buyurtmalar, sep="\n")

# Amaliyot 2 masala

# print("Maxsulotlar va ularning nomlarini kiritadigan dastur")
# maxsulotlar = {}
# while True:
#     nom = input("Maxsulot nomini kiriting: ")
#     narx = input(f"{nom}ning narxini kiriting: ")
#     maxsulotlar[nom] = int(narx)
#     takrorlash = input("Yana maxsulot qo'shasizmi? (ha/yo'q): ")
#     if takrorlash.lower() != 'ha':
#         break
# print("Maxsulotlaringiz:")
# for nom, narx in maxsulotlar.items():
#     print(f"{nom}: {narx} so'm")

# Amaliyot 3 masala

e_bozor = {
	'olma' : 10000,
    'uzum' : 20000,
    'anjir' : 30000,
    'shaftoli' : 40000,
    'olcha' : 50000,
    'nok' : 60000,
    'anor' : 70000,
    'mandarin' : 90000,
    'limon' : 100000,
    'kivi' : 110000,
    'tarvuz' : 120000,
    'qovun' : 130000,
    'apelsin' : 140000,
    'banan' : 150000,
    'xurmo' : 160000
    }
print("E-BOZORGA XUSH KELIBSIZ!")
savatcha = {}
while True:
    buyurtma = input("Qanday mahsulot sotib olishingiz kerak? (dasturni to'xtatish uchun 'exit' deb yozing): ")
    if buyurtma.lower() == 'exit':
        break
    mahsulot = buyurtma.lower()
    if mahsulot in e_bozor:
        miqdor = int(input(f"{mahsulot}ning qancha kilogrammini sotib olmoqchisiz? "))
        if mahsulot in savatcha:
            savatcha[mahsulot] += miqdor
        else:
            savatcha[mahsulot] = miqdor
    else:
        print(f"Kechirasiz, {mahsulot} mahsuloti mavjud emas.")
print("Savatchangiz:")
for mahsulot, miqdor in savatcha.items():
    narx = e_bozor[mahsulot] * miqdor 
    print(f"{mahsulot}: {miqdor} kg - {narx} so'm")