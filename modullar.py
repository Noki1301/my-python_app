# import avto_info_mod as aim # bu modul ismi uzun bulsa qisqartirish

# avto1 = aim.avto_info('GM', 'Malibu', 'qora', 'avtomat', 2018, 20000)
# print(f"{avto1['rang'].title()} {avto1['kompaniya']} {avto1['model']} {avto1['yil']} {avto1['korobka']} {avto1['narh']} $")

#from avto_info_mod import avto_info as ai, avto_kirit as ak, avto_chiqar as ac # bu moduldan funksiyani chaqirib olish 
# from avto_info_mod import * # bu moduldan barcha funksiyalarni chaqirib olish lekin tavsiya etilmaydi
# avto1 = avto_info('GM', 'Malibu', 'qora', 'avtomat', 2018, 20000)
# print(f"{avto1['rang'].title()} {avto1['kompaniya']} {avto1['model']} {avto1['yil']} {avto1['korobka']} {avto1['narh']} $")
# avto2 = avto_info('GM', 'Gentra', 'qora', 'avtomat', 2018, 15000)
# print(f"{avto2['rang'].title()} {avto2['kompaniya']} {avto2['model']} {avto2['yil']} {avto2['korobka']} {avto2['narh']} $")	

# import math #python default modullariga misol 
# x = 400
# print(math.sqrt(x))
# print(math.pow(10, 2))
# print(math.pi)
# print(math.log2(8))
# print(math.log10(100))

import random as r
#randint funksiyasi misol
# son = r.randint(1, 100)
# print(son)

#choice funksiyasi misol
# ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', "G'ani"]
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ism))#bu matnlarga misol 

#choice funksiyasi misol
# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))

#shuffle funksiyasi misol
# x = list(range(1, 11))
# print(x)
# r.shuffle(x)
# print(x)