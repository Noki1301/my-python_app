# def salom_ber(ism):
# 		"""Foydalanuvchining ismini qabul qilib, salom beruvchi funksiya."""
# 		print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# salom_ber("Ali")
# salom_ber("Vali")

# def toliq_ism(ism, familiya):
# 		"""Foydalanuvchining ismi va familiyasini qabul qilib, to'liq ismini qaytaruvchi funksiya."""
# 		return f"{ism.title()} {familiya.title()}"
# talaba1 = toliq_ism("ali", "valiyev")
# talaba2 = toliq_ism("vali", "valiyev")
# print(talaba1)
# print(talaba2)

# def yosh_xisobla(ism,tugilgan_yil):
# 		"""Foydalanuvchining ismi va tug'ilgan yilini qabul qilib, yoshini qaytaruvchi funksiya."""
# 		print(f"{ism.title()} {2025-tugilgan_yil} yoshda")
# yosh_xisobla("ali",1996)

# def yosh_xisobla(ism,tugilgan_yil,joriy_yil=2025):
# 	"""Foydalanuvchining ismi va tug'ilgan yilini qabul qilib,
# 	yoshini qaytaruvchi funksiya."""
# 	print(f"{ism.title()} {joriy_yil-tugilgan_yil} yoshda")
# yosh_xisobla("ali",1996)
# yosh_xisobla("vali",1992)

# Amaliyot 1 masala
# def foydalanuvchi_ismi_yoshi(ism, yosh):
#     """Foydalanuvchining ismi va yoshini qabul qilib, tug'ilgan yilini hisoblaydi."""
#     hozirgi_yil = 2025 
#     tugilgan_yil = hozirgi_yil - yosh
#     print(f"{ism.title()} {tugilgan_yil}-yilda tug'ilgan.")

# foydalanuvchi_ismi_yoshi("nodir", 30)

# Amaliyot 2 masala
# def son(son1):
# 		"""Foydalanuvchidan son qabul qilib, uning kvadratini va kubini hisoblaydi."""
# 		return son1 ** 2, son1 ** 3
# son1 = int(input("Istalgan sonni kiriting: "))
# kvadrat, kub = son(son1)
# print(f"{son1} Kvadrati: {kvadrat}, Kubi: {kub}")

# Amaliyot 3 masala
# def son(son):
# 	"""Foydalanuvchidan son qabul qilib, uning toq yoki juftligini tekshiradi."""
# 	if son % 2 == 0:
# 		print(f"{son} soni juft son")
# 	else:
# 		print(f"{son} soni toq son")
# son(int(input("Istalgan sonni kiriting: ")))

# Amaliyot 4 masala
# def ikkita_son(son1, son2):
# 		"""Foydalanuvchidan ikkita son qabul qilib,ularning kattasini konsolga chiqaradi."""
# 		if son1 > son2:
# 			print(f"{son1} katta")
# 		elif son1 < son2:
# 			print(f"{son2} katta")
# 		else:
# 			print(f"Sonlar teng")
# ikkita_son(int(input("Birinchi sonni kiriting: ")), int(input("Ikkinchi sonni kiriting: ")))

# Amaliyot 5 masala
# def sonlar_kiriting(x,y):
# 	"""Foydalanuvchidan son qabul qilib,uni darajaga ko'taruvchi funksiya."""
# 	return x ** y
# x = int(input("Istalgan sonni kiriting: "))
# y = int(input("Darajani kiriting: "))
# print(sonlar_kiriting(x,y))

# Amaliyot 6 masala
# def sonlar_kiriting(x,y):
# 	"""Foydalanuvchidan son qabul qilib,uni faqat kvadratiga ko'taruvchi funksiya."""
# 	return x ** y
# x = int(input("Istalgan sonni kiriting: "))
# print(sonlar_kiriting(x,2))

# Amaliyot 7 masala
# def bolinishni_tekshir(son):
#     """Sonni 2 dan 10 gacha bo'lgan sonlarga bo'linishini tekshiruvchi funksiya"""
#     for i in range(2, 11):
#         if son % i == 0:
#             print(f"{son} {i} ga qoldiqsiz bo'linadi")

# # Foydalanuvchidan son so'raymiz
# son = int(input("Biror son kiriting: "))
# bolinishni_tekshir(son)
