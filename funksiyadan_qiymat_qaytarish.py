# def toliq_ism(ism, familiya):
# 	"""
# 	Bu funksiya ism va familiyani birlashtirib to'liq ismni qaytaradi.
# 	"""
# 	toliq_ismi = f"{ism} {familiya}"
# 	return toliq_ismi.title()

# talaba1 = toliq_ism("ali", "valiyev")
# talaba2 = toliq_ism("vali", "valiyev")
# print(f"Darsga qatnashmagan talabalar: {talaba1} va {talaba2}.")

# def toliq_ism(ism, familiya, otasining_ismi = ""):
# 	"""
# 	Bu funksiya ism va familiyani birlashtirib to'liq ismni qaytaradi.
# 	"""
# 	if otasining_ismi:
# 		toliq_ismi = f"{ism} {otasining_ismi} {familiya}"
# 	else:
# 		toliq_ismi = f"{ism} {familiya}"
# 	return toliq_ismi.title()
# talaba1 = toliq_ism("ali","valiyevich","valiyev")
# talaba2 = toliq_ism("vali","valiyev")
# print(f"Darsga qatnashmagan talabalar: {talaba1} va {talaba2}.")

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi = None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
# avto1 = avto_info('GM', 'Malibu', 'qora', 'avtomat', 2020, 40000)
# avto2 = avto_info('GM', 'Malibu', 'qizil', 'mexanik', 2021, 45000)
# avto3 = avto_info('GM', 'Malibu', 'oq', 'avtomat', 2022)
# avtolar = [avto1, avto2, avto3]
# print("Onlayn bozordagi avtomobillar:")
# for avto in avtolar:
#     if avto["narh"]:
#         narh = avto["narh"]
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang'].title()} {avto['kompaniya']} {avto['model']} "
# 					f"{avto['yil']}-yil, {avto['korobka']} korobka, narhi: {narh} $")

# def oraliq(min_son, max_son, qadam=1):
#     """
#     Bu funksiya berilgan oraliqdagi sonlar ro'yxatini qaytaradi.
#     """
#     sonlar = []
#     while min_son < max_son:
#         sonlar.append(min_son)
#         min_son += qadam
#     return sonlar

# print(f"oraliq(0,10) natijasi: {oraliq(0,10) if oraliq(0,10) else 'Oraliqda sonlar mavjud emas.'}")
# print(f"oraliq(10,21,2) natijasi: {oraliq(10,21,2) if oraliq(10,21,2) else 'Oraliqda sonlar mavjud emas.'}")

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi = None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
# print("Onlayn bozordagi avtomobillar ruyxatini shakllantiramiz:")
# avtolar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting:", end=' ')
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narhi = input("Narhi: ")
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#     javob = input("Yana avto qo'shasizmi? (ha/yo'q)")
#     if javob.lower() != 'ha':
#         break
# print("\nOnlayn bozordagi avtomobillar:")
# for avto in avtolar:
#     if avto["narh"]:
#         narh = avto["narh"]
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang'].title()} {avto['kompaniya'].title()} {avto['model'].title()} "
#           f"{avto['yil']}-yil, {avto['korobka'].title()} korobka, narhi: {narh} $")

# Amaliyot 1-masala

# def foydalanuvchi_info(ism, familiya, tugilgan_yil, tugilgan_joyi, email=None, tel=None):
#     info = {
#         'ism': ism.title(),
#         'familiya': familiya.title(),
#         'tugilgan_yil': tugilgan_yil,
#         'tugilgan_joyi': tugilgan_joyi.title(),
#         'email': email,
#         'telefon': tel
#     }
#     return info
# print("Foydalanuvchilar haqida ma'lumotlarni kiriting:")
# foydalanuvchilar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting:", end=' ')
#     ism = input("Ismingiz: ")
#     familiya = input("Familiyangiz: ")
#     tugilgan_yil = input("Tug'ilgan yilingiz: ")
#     tugilgan_joyi = input("Tug'ilgan joyingiz: ")
#     email = input("Email: ")
#     tel = input("Telefon raqami: ")
#     foydalanuvchilar.append(foydalanuvchi_info(ism, familiya, tugilgan_yil, tugilgan_joyi, email, tel))
#     javob = input("Yana foydalanuvchi qo'shasizmi? (ha/yo'q) ")
#     if javob.lower() != 'ha':
#         break
# print("\nFoydalanuvchilar ro'yxati:")
# for foydalanuvchi in foydalanuvchilar:
#     print(f"{foydalanuvchi['ism']} {foydalanuvchi['familiya']}, "
#           f"Tug'ilgan yili: {foydalanuvchi['tugilgan_yil']}, "
#           f"Tug'ilgan joyi: {foydalanuvchi['tugilgan_joyi']}, "
#           f"Email: {foydalanuvchi['email']}, "
#           f"Telefon: {foydalanuvchi['telefon']}")

# Amaliyot 2-masala

# def eng_katta_son():
#     """Bu funksiya sonlar 3 ta son qabul qilib eng katta sonni qaytaradi."""
#     sonlar = input("3 ta son kiriting (vergul bilan ajrating): ")
#     sonlar = [int(x) for x in sonlar.split(',')]
#     return max(sonlar)
# print(f"Kiritilgan sonlar ichida eng katta son: {eng_katta_son()}")

# def  aylananing_parametrlarini_hisobla(radius,yuzi,diametri,perimetri):
#     """
#     Bu funksiya aylananing radiusini qabul qilib,
#     aylananing parametrlarini hisoblaydi.
#     """
#     aylananing_parametrlar = {
#         'radius': radius,
#         'yuzi': yuzi,
#         'diametri': diametri,
#         'perimetri': perimetri
#     }
#     return aylananing_parametrlar
# print("Aylananing parametrlarini hisoblaymiz:")
# radius = float(input("Aylananing radiusini kiriting: "))
# yuzi = 3.14*radius**2
# diametri = 2*radius
# perimetri = 2*3.14*radius
# print(f"Aylananing radiusi: {radius}, Yuzi: {yuzi}, Diametri: {diametri}, Perimetri: {perimetri}")

# def tub_sonlar_ruyhatini_hisobla(min,max):
# 	"""Bu funksiya oraliqdagi tub sonlar ro'yxatini qaytaradi."""
# 	tub_sonlar = []
# 	for son in range(min, max + 1):
# 		if son > 1:
# 			for i in range(2, son):
# 				if son % i == 0:
# 					break
# 			else:
# 				tub_sonlar.append(son)
# 	return tub_sonlar
# print("Tub sonlar ro'yxatini hisoblaymiz:")
# min = int(input("Nechanchi sondan boshlaymiz: "))
# max = int(input("Nechanchi sondan tugaymiz: "))
# print(f"{min} dan {max} gacha bo'lgan tub sonlar: {tub_sonlar_ruyhatini_hisobla(min, max)}")

def fibonachi_ketma_ketligi(n):
    """Bu funksiya Fibonachchi ketma-ketligini hisoblaydi."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonachi = [0, 1]
    for i in range(2, n):
        fibonachi.append(fibonachi[i-1] + fibonachi[i-2])
    
    return fibonachi
print("Fibonachchi ketma-ketligini hisoblaymiz:")
n = int(input("Nechta son kiritmoqchisiz: "))
print(f"Fibonachchi ketma-ketligi: {fibonachi_ketma_ketligi(n)}")