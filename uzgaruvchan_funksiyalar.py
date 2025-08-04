# def summa(*sonlar):#bu *args ga misol bu son ko'rinishidagi istalgancha sonlarni qabul qiladi
# 	
# 	"""Bu funksiya sonlar ro'yxatini yig'indisini hisoblaydi."""
# 	yigindisi = 0
# 	for son in sonlar:
# 		yigindisi += son
# 	return yigindisi
# # yoki return sum(sonlar) bu ham ishlaydi
# print(summa(1,2,3,4,5))
# print(summa(1,2,3,4,5,6,7,8,9,10))
# print(summa(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))

# def summa(x,y,*sonlar):
# 	"""Bu funksiya sonlar ro'yxatini yig'indisini hisoblaydi."""
# 	return sum(sonlar) 
# print(summa(1,2,3,4,5))
# print(summa(1,2,3,4,5,6,7,8,9,10))
# print(summa(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
# print(summa(2)) bu hato sababi majburiy 2 argument kiritilishi shart bu funksiyada 

# def avto_info(kompaniya,model,**malumotlar):#**kwargs ga misol bu matn ko'rinishidagi istalgancha malumotlarni qabul qiladi
# 	"""Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaradi"""
# 	malumotlar['kompaniya'] = kompaniya
# 	malumotlar['model'] = model
# 	return malumotlar
# avto1 = avto_info("GM","Malibu", rang="qora", narh=20000)
# avto2 = avto_info("Honda", "Accord", rang="qizil", yil=2015, narh=18000)
# print(avto1)
# print(avto2)

# def sonlar_kupaytmasi(*sonlar):
# 	kupaytma = 1
# 	for son in sonlar:
# 		kupaytma *= son
# 	return kupaytma
# print(sonlar_kupaytmasi(1,2))
# print(sonlar_kupaytmasi(1,2,3))
# print(sonlar_kupaytmasi(1,2,3,4))

def talaba_malumotlari(ism,familiya,**malumotlar):
	malumotlar['ism'] = ism
	malumotlar['familiya'] = familiya
	return malumotlar
talaba1 = talaba_malumotlari("Alijon","Toshmatov",yosh=20,fakultet="matematika",kurs=2)
talaba2 = talaba_malumotlari("Valijon","Aliyev",yosh=21,fakultet="matematika",kurs=1)
print(f"Talaba {talaba1['ism']} {talaba1['familiya']} {talaba1['yosh']} yoshda {talaba1['fakultet'].title()} fakultetida {talaba1['kurs']} kursda o'qiydi")
print(talaba2)