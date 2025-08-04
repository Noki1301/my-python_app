# input
# ism = input("Ismingiz nima?\n")
# savol = (f"Salom {ism.title()}. Yoshingiz nechida?\n")
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yingiz necha metr?\n")
# height = float(height)
# print(f"Assalomu alaykum {ism.title()}, {yosh} yoshdasiz. {height} metr ekaningizni bilaman.")

# while tsikli
# son = 1
# while son<=5:
#     print(son, end=' ')
#     son+=1
# print("Dastur tugadi.")

# print("Kiritilgan sonning kvadratini hisoblaydigan dastur.")
# savol = "Istalgan sonni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing)\n"
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(f"{float(qiymat)**2}")
# print("Dastur tugadi.")

# ishora 
# print("Kiritilgan sonning kvadratini hisoblaydigan dastur.")
# savol = "Istalgan sonni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing)\n"
# ishora = True
# while ishora:
# 	ishora = input(savol)
# 	if ishora == 'exit':
# 		ishora = False
# 	else:
# 		print(f"{float(ishora)**2}")
# print("Dastur tugadi.")

# break
# print("Kiritilgan sonning kvadratini hisoblaydigan dastur.")
# savol = "Istalgan sonni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing)\n"
# while True:
# 	ishora = input(savol)
# 	if ishora == 'exit':
# 		break
# 	else:
# 		print(f"{float(ishora)**2}")
# print("Dastur tugadi.")

# break for 
# sonlar = list(range(1,11))
# for son in sonlar:
# 	if son == 5:
# 		break
# 	print(f"{son} ning kvadrati {son**2} ga teng.")

# continue
# sonlar = list(range(1,11))
# for son in sonlar:
# 	if son == 5:
# 		continue
# 	print(f"{son} ning kvadrati {son**2} ga teng.")

# continue while
# son = 0
# while son <10:
# 	son += 1
# 	if son%2!=0:# son % 2 — bu modul (qoldiq) operatori bo‘lib, sonni 2 ga bo‘lgandagi qoldiqni hisoblaydi.
# # Agar son % 2 == 0 bo‘lsa → bu juft son (chunki 2 ga bo‘linadi, qoldiq 0).
# # Agar son % 2 != 0 bo‘lsa → bu toq son (chunki 2 ga bo‘linmaydi, qoldiq 1).
# 		continue
# 	print(son)

# infinite loop
# son = 0 
# while son <10:# bu shart to'g'ri bo'lsa, tsikl davom etadi aks holda to'xtamaydi misol uchun while son >0: bulsa bu tsikl abadiy davom etadi
# 	son += 1 #bu qolib ketsa abadiy tsikl to'xtamaydi
# 	if son%2!=0:
# 		continue
# 	else:
# 		print(son)

# Amaliyot 1 - masala

# print("Yaxshi ko'rgan kitoblaringizni kiriting.")
# eslatma = "Dasturdan chiqish uchun 'stop' deb yozing.\n"
# kitoblar = []
# while True:
# 	kitob = input("Kitob nomini kiriting:")
# 	if kitob == 'stop':
# 		break
# 	kitoblar.append(kitob)
# print("Siz yaxshi ko'rgan kitoblaringiz:")
# for kitob in kitoblar:
# 	print(kitob)

# Amaliyot 2 - masala
# break uslubida 
# print("Yoshingizni kiriting muzeyga kirish uchun bilet narxlari chiqariladi.")
# savol = "Yoshingizni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit'yoki 'quit' deb yozing)"
# while True:
# 	yosh = input(savol)
# 	if  yosh == 'exit' or yosh == 'quit':
# 		break
# 	yosh = int(yosh)
# 	if yosh < 7:
# 		print(f"Sizning yoshingiz {yosh} da, muzeyga kirish uchun bilet narxi 2000 so'm.")
# 	elif yosh < 18:
# 		print(f"Sizning yoshingiz {yosh} da, muzeyga kirish uchun bilet narxi 3000 so'm.")
# 	elif yosh < 65:
# 		print(f"Sizning yoshingiz {yosh} da, muzeyga kirish uchun bilet narxi 10000 so'm.")
# print("Maroqli hordiq chiqaring! Muzeyimizga tashrif buyurganingiz uchun rahmat!")

# flag(ishora) uslubida
# print("Yoshingizni kiriting, muzeyga kirish uchun bilet narxlari chiqariladi.")

# active = True
# while active:
#     yosh = input("Yoshingizni kiriting (dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing): ")
#     if yosh == 'exit' or yosh == 'quit':
#         active = False
#     else:
#         yosh = int(yosh)
#         if yosh < 7:
#             print(f"{yosh} yosh — 2000 so'm.")
#         elif yosh < 18:
#             print(f"{yosh} yosh — 3000 so'm.")
#         elif yosh < 65:
#             print(f"{yosh} yosh — 10000 so'm.")
#         else:
#             print(f"{yosh} yosh — bepul.")

# print("Muzeyimizga tashrif uchun tashakkur!")

# while input uslubida
# print("Yoshingizni kiriting, muzeyga kirish uchun bilet narxlari chiqariladi.")

# yosh = ""
# while yosh != 'exit' and yosh != 'quit':
#     yosh = input("Yoshingizni kiriting (dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing): ")
#     if yosh != 'exit' and yosh != 'quit':
#         yosh = int(yosh)
#         if yosh < 7:
#             print(f"{yosh} yosh — 2000 so'm.")
#         elif yosh < 18:
#             print(f"{yosh} yosh — 3000 so'm.")
#         elif yosh < 65:
#             print(f"{yosh} yosh — 10000 so'm.")
#         else:
#             print(f"{yosh} yosh — bepul.")

# print("Muzeyimizga tashrif uchun tashakkur!")

# Amaliyot: 3-masala

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'Exit':
        break
    qiymat = float(qiymat)
    if qiymat < 0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")