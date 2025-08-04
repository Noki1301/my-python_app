# car_0 = {"model":"kia","rang":"oq"}
# print(car_0["model"])
# print(car_0["rang"])

# eng_uz = {"car":"mashina","house":"uylar","book":"kitob"}
# print(eng_uz["car"]	)
# print(eng_uz["house"])
# print(eng_uz["book"])

# mevalar = {"olma":10000,"anjir":20000,"uzum":30000,"shaftoli":40000}
# print(f"Olma narxi {mevalar['olma']} so'm")
# print(f"Anjir narxi {mevalar['anjir']} so'm")
# print(f"Uzum narxi {mevalar['uzum']} so'm")
# print(f"Shaftoli narxi {mevalar['shaftoli']} so'm")

# talaba = {"ism":"Alijon","familiya":"Toshmatov","yosh":20,"fakultet":"matematika","kurs":2}
# print(f"Talaba {talaba['ism']} {talaba['familiya']} {talaba['yosh']} yoshda {talaba['fakultet'].title()} fakultetida {talaba['kurs']} kursda o'qiydi")

# talaba['kurs'] = 3
# print(f"Talaba {talaba['ism']} {talaba['familiya']} {talaba['yosh']} yoshda {talaba['fakultet'].title()} fakultetida {talaba['kurs']} kursda o'qiydi")


# talaba_1 = {}
# talaba_1['ism'] = 'Alijon'
# talaba_1['familiya'] = 'Toshmatov'
# talaba_1['yosh'] = 20
# talaba_1['fakultet'] = 'matematika'
# talaba_1['kurs'] = 2
# print(talaba_1)
# del talaba_1['yosh']
# print(talaba_1)

# telefonlar = {
# 	"ali": "+998901234567",
# 	"vali": "+998901234568",
# 	"hasan": "+998901234569",
# 	"husan": "+998901234570",
# }
# get methodi lug'atdan qiymatni olish uchun ishlatiladi
# print(telefonlar.get("ali"))
# print(telefonlar.get("hasan"))
# print(telefonlar.get("aziz","Bunday ism mavjud emas"))
# print(telefonlar.get("anvar","Bunday ism mavjud emas"))

# Amaliyot 1 - masala

# oila = {
# 	"ota":{
# 		"ism":"Ali",
# 		"yosh":45,
# 		"t_yil":1975,
# 		"tug'ilgan_joy":"Toshkent"
# 	},
# 	"ona":{
# 		"ism":"Gulnoza",
# 		"yosh":45,
# 		"t_yil":1975,
# 		"tug'ilgan_joy":"Toshkent"
# 	},
# 	"bobo":{
# 		"ism":"Olim",
# 		"yosh":45,
# 		"t_yil":1945,
# 		"tug'ilgan_joy":"Toshkent"
# 	},
# 	"uka":{
# 		"ism":"Saki",
# 		"yosh":15,
# 		"t_yil":2010,
# 		"tug'ilgan_joy":"Toshkent"
# 	}
# }
# print(f"Otamning ismi {oila['ota']['ism']} tug'ilgan yili {oila['ota']['t_yil']} tug'ilgan joyi {oila['ota']['tug\'ilgan_joy']}")
# print(f"Onamning ismi {oila['ona']['ism']} tug'ilgan yili {oila['ona']['t_yil']} tug'ilgan joyi {oila['ona']['tug\'ilgan_joy']}")
# print(f"Bobomning ismi {oila['bobo']['ism']} tug'ilgan yili {oila['bobo']['t_yil']} tug'ilgan joyi {oila['bobo']['tug\'ilgan_joy']}")
# print(f"Ukamning ismi {oila['uka']['ism']} tug'ilgan yili {oila['uka']['t_yil']} tug'ilgan joyi {oila['uka']['tug\'ilgan_joy']}")

# Amaliyot 2 - masala

# oila_taomlar ={
# 	"otam":"jiz",
# 	"onam":"osh",
# 	"singlim":"somsa",
# 	"ukam":"manti"
# }
# print(f"Otamning sevimli taomi {oila_taomlar['otam']}")
# print(f"Onamning sevimli taomi {oila_taomlar['onam']}")
# print(f"Singlimning sevimli taomi {oila_taomlar['singlim']}")
# print(f"Ukamning sevimli taomi {oila_taomlar['ukam']}")

# Amaliyot 3 - masala

# python_lugat = {
# 	"integer":"butun son",
# 	"float":"o'nlik son",
# 	"string":"matn",
# 	"boolean":"rost yoki yolg'on",
# 	"list":"ro'yxat",
# }
# print(python_lugat["integer"])
# print(python_lugat["float"])
# print(python_lugat["string"])
# print(python_lugat["boolean"])
# print(python_lugat["list"])

# Amaliyot 4 - masala

lugat = {
    "integer": "butun son",
    "float": "o'nlik son",
    "string": "matn",
    "boolean": "rost yoki yolg'on",
    "list": "ro'yxat",
    "tuple": "o'zgarmas ro'yxat",
    "dictionary": "lug'at",
    "set": "to'plam"
}

# suz = input("Kalit so'z kiriting: ").lower()

# if suz in lugat:
#     print(f"{suz} so‘zi lug‘atda mavjud. Unga mos tarjimasi: {lugat[suz]}")
# else:
#     print(f"{suz} so‘zi lug‘atda mavjud emas.")

# Amaliyot 5 - masala

kalit = input("Kalit so'z kiriting:").lower()
tarjima = lugat.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")

