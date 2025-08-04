# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh < 4:
# 	narx = 0
# elif yosh < 12:
# 	narx = 5000
# elif yosh < 18:
# 	narx = 10000
# else:
# 	narx = 20000
# print(f"Sizga kirish {narx} so'm")

# kun = input("Bugun nima kun?>>>")
# if kun.lower() == "shanba" or kun.lower() == "yakshanba":
# 	print("Bugun dam olish kuni")
# else:
# 	print("Bugun ish kuni")

# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati necha gradus?"))
# if kun.lower() == "yakshanba" and harorat>=30:
# 	print("Cho'milgani ketdik")
# elif kun.lower() == "yakshanba" and harorat<30:
# 	print("Cho'miladigan kun emas")
# else:
# 	print("Cho'miladigan kun emas, ish kuni")

# narh = 25000
# choy = True
# salat = True
# if choy and salat:
# 	narh = narh + 10000
# elif choy or salat:
# 	narh = narh + 5000
# print(f"Jami {narh} so'm")

# narh = 25000
# choy = True
# salat = False
# non = True
# kampot = False
# assorti = True

# if choy:
# 	print("Mijoz choy oldi")
# 	narh += 5000
# if salat:
# 	print("Mijoz salat oldi")
# 	narh += 10000
# if non:
# 	print("Mijoz non oldi")
# 	narh += 3000
# if kampot:
# 	print("Mijoz kampot oldi")
# 	narh += 20000
# if assorti:
# 	print("Mijoz assorti oldi")
# 	narh += 15000
# print(f"Jami {narh} so'm")

# menu = ["osh", "shashlik", "somsa", "manti", "lag'mon"]
# "manti" in menu
# print("palov" in menu)

# menu = ["osh", "shashlik", "somsa", "manti", "lag'mon"]
# buyurtma = input("Nima buyurtma qilasiz?>>>")
# if buyurtma in menu:
# 	print("Buyurtma qabul qilindi")
# else:
# 	print("Kechirasiz, bizda bunday taom yo'q")

# menu = ["osh", "shashlik", "somsa", "manti", "lag'mon"]
# buyurtmalar =["osh", "somsa", "lag'mon","non", "choy"]
# for buyurtma in buyurtmalar:
# 	if buyurtma in menu:
# 		print(f"Menyu ichida {buyurtma} bor")
# 	else:
# 		print(f"Menyu ichida {buyurtma} yo'q")	

# Amaliyot 1 - masala
# son = float(input("Son kiriting>>>"))
# if son % 2 == 0:
# 	print("Rahmat!")
# else:
# 	print("Rahmat lekin bu son juft emas!")

# Amaliyot 2 - masala
# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh < 4 or yosh > 60:
# 	print("Sizga kirish bepul")
# elif yosh < 18:
# 	print("Sizga kirish 10000 so'm")
# else:
# 	print("Sizga kirish 20000 so'm")

# Amaliyot 3 - masala
# birinchi_son = int(input("Birinchi son kiriting>>>"))
# ikkinchi_son = int(input("Ikkinchi son kiriting>>>"))
# if birinchi_son > ikkinchi_son:
# 	print(f"{birinchi_son} soni Katta" )
# elif birinchi_son < ikkinchi_son:
# 	print(f"{ikkinchi_son} soni Katta")
# elif birinchi_son == ikkinchi_son:
# 	print(f"Ikkita son teng")

# Amaliyot 4 - masala
# mahsulotlar = ["non", "un", "yog'", "sut", "tuxum", "guruch", "piyoz", "kartoshka", "shakar", "choy"]
# savat = []

# print("Kamida 5 ta mahsulot kiriting:")
# for i in range(5):
#     mahsulot = input(f"{i+1}-mahsulot: ").lower()
#     savat.append(mahsulot)

# print("\nDo'konimizda bor mahsulotlar:")
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot.title()} do'konimizda bor.")
#     else:
#         print(f"{mahsulot.title()} do'konimizda yo'q.")

# Amaliyot 5 - masala
# mahsulotlar = ["non", "un", "yog'", "sut", "tuxum", "guruch", "piyoz", "kartoshka", "shakar", "choy"]
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []

# print("Iltimos, 5 ta mahsulot kiriting:")
# for i in range(5):
#     mahsulot = input(f"{i+1}-mahsulot: ").lower()
#     savat.append(mahsulot)

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if not mavjud_emas:
#     print("\nSiz so‘ragan barcha mahsulotlar do‘konimizda bor.")
# else:
#     print("\nQuyidagi mahsulotlar do‘konimizda yo‘q:")
#     for mahsulot in mavjud_emas:
#         print(f"- {mahsulot.title()}")

# Amaliyot 6 - masala
# foydalanuvchilar = ["ali", "vali", "hasan", "husan"]
# login = input("Yangi login tanlang:>>>").lower()
# for foydalanuvchi in foydalanuvchilar:
# 	if login == foydalanuvchi:
# 		print("Bu login band, yangi login tanlang")
# 		break
# else:
# 	foydalanuvchilar.append(login)
# 	print(f"Xush kelibsiz {login.title()}!")

# Amaliyot 7 - masala
# butun_son = int(input("Butun son kiriting:>>>"))

# for i in range(2,11):
# 	if not (butun_son % i):
# 		print(f"{butun_son} soni {i} ga qoldiqsiz bo'linadi")


