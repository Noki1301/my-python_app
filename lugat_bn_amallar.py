# # talaba_0 = {
# # 		"ism": "Ali",
# # 		"familiya": "Valiyev",
# # 		"yosh": 20,
# # 		"kurs": 2,
# # 		"fakultet": "Informatika",
# # 		"guruh": "I-202",
# # 		"baholar": {
# # 			"matematika": 85,
# # 			"fizika": 90,
# # 			"informatika": 95
# # 		}
# # }
# # print("Talaba ma'lumotlari:")
# # print("Ism:", talaba_0.items())
# # for kalit, qiymat in talaba_0.items():
# #     print(f"{kalit}: {qiymat}")

# telefonlar = {
# 		"Ali": "iphone 12",
# 		"Vali": "samsung s21",
# 		"Hasan": "xiaomi redmi note 10",
# 		"Husan": "oppo a54",
# 		"Zarina": "nokia 3310",
# 		"Malika": "realme 8",
# 		"Olim": "iphone 12",
# 		"Shahnoza": "samsung s21",
# 		"Aziz": "xiaomi redmi note 10",
# 		"Nilufar": "oppo a54",
# 		"Jasur": "nokia 3310",
# 		"Shokir": "realme 8",
# 		"Yulduz": "iphone 12",
# 		"Bobur": "samsung s21",
# 		"Farhod": "xiaomi redmi note 10",
# 		"Olim": "oppo a54",
# 		"Shahnoza": "nokia 3310",
# 		"Aziz": "realme 8"
# }
# # for k,q in telefonlar.items():
# # 	print(f"{k.title()}ning telefoni: {q}")

# mahsulotlar = {
# 		"olma": {
			
# 			"narx": 2000
# 		},
# 		"banan": {
			
# 			"narx": 1500
# 		},
# 		"apelsin": {
			
# 			"narx": 2500
# 		},
# 		"shaftoli": {
			
# 			"narx": 3500
# 		},
# 		"uzum": {
			
# 			"narx": 3000
# 		},
# 		"anjir": {
			
# 			"narx": 4000
# 		},
# 		"nok": {
			
# 			"narx": 4500
# 		},
# 		"tarvuz": {
			
# 			"narx": 5000
# 		},
# 		"qovun": {
			
# 			"narx": 6000
# 		},
# 		"limon": {
			
# 			"narx": 1800
# 		}
# 	}
# # print(mahsulotlar.keys())
# # print("Mahsulotlar:")
# # for mahsulot in mahsulotlar:
# # 	print(mahsulot.title())
# bozorlik = ['olma', 'banan', 'apelsin', 'shaftoli', 'uzum', 'anjir', 'nok', 'tarvuz', 'qovun', 'limon','kivi', 'mandarin', 'xurmo', 'gilos', 'malina', 'qizil olma', 'sariq olma', 'yashil olma', 'qora uzum', 'oq uzum', 'qizil uzum']
# # for mahsulot in mahsulotlar:
# # 	if mahsulot in bozorlik:
# # 		print(f"{mahsulot.title()} bozorlikda mavjud.{mahsulotlar[mahsulot]} so'm")

# # for mahsulot1 in bozorlik:
# # 	if mahsulot1 not in mahsulotlar:
# # 		print(f"Kechirasiz, {mahsulot1} bozorlikda yo'q")
# # 	else:
# # 		print(f"{mahsulot1.title()} {mahsulotlar[mahsulot1]} so'm")
# # print("Bozorlikdagi mahsulotlar:")
# # for mahsulot in sorted(mahsulotlar):
# # 		narx = mahsulotlar[mahsulot]['narx']
# # 		print(f"{mahsulot.title()} - {narx} so'm")

# # print(mahsulotlar.values())

# print("Foydalanuchilar quyidagi telefonlardan foydalanishadi:")
# # for tel in telefonlar.values():
# # 	print(tel.title())
# for tel in set(telefonlar.values()):
# 	print(f"{tel.title()} telefonlaridan foydalanishadi.")

# Amaliyot 1 - masala

# python_lugat = {
# 		"print": "ekranga chiqarish",
# 		"input": "ma'lumot kiritish",
# 		"if": "agar",
# 		"else": "aks holda",
# 		"elif": "aks holda",
# 		"for": "for tsikli",
# 		"while": "while tsikli",
# 		"list": "ro'yxat",
# 		"dict": "lug'at",
# 		"tuple": "o'zgarmas ro'yxat",
# 		"set": "o'zgarmas ro'yxat",
# 		"int": "butun son",
# 		"float": "o'nlik son",
# 		"string": "matn",
# 		"bool": "rost yoki yolg'on",
# 		"import": "kutubxonani chaqirish",
# 		"def": "funksiya aniqlash",
# 		"class": "sinf aniqlash",
# 		"return": "funksiyadan qiymat qaytarish",
# 		"break": "tsiklni to'xtatish",
# 		"continue": "tsiklni davom ettirish",
# 		"global": "global funksiya",
# 		"nonlocal": "nonlocal funksiya",
# 		"lambda": "lambda funksiya",
# 		"try": "try-except bloki",
# 		"except": "try-except bloki",
# 		"finally": "try-except bloki",
# 		"raise": "try-except bloki",
# 		"with": "with bloki",
# 		"as": "with bloki",
# 		"yield": "yield funksiya",
# 		"nonlocal": "nonlocal funksiya",
# 		"assert": "assert funksiya"
# }
# print("Python dasturlash tilidagi funksiyalar va operatorlar:")
# for funksiya, qiymat in sorted (python_lugat.items()):
# 	print(f"{funksiya.title()}: {qiymat}")

davlatlar = {
	"uzbekistan": "toshkent",
	"russiya": "moskva",
	"qirg'izstan": "bishkek",
	"aqsh": "washington",
	"fransiya": "parij",
	"germaniya": "berlin",
	"italiya": "rim",
	"ispaniya": "madrid",
	"turkiya": "ankara",
	"japoniya": "tokio",
	"janubiy koreya": "seul",
	"kanada": "ottava",
	"avstraliya": "kanberra",
	"braziliya": "brasilia",
	"indiya": "delhi",
	"pakistan": "islamobod",
	"indoneziya": "jakarta",
	"malayziya": "kuala-lumpur",
	"singapur": "singapur",
	"misr": "qohira",
	"arabiston": "riyod",
	"saudiya arabistoni": "riyod",
	"emirliklar": "abu-dabi",
	"yaponiya": "tokio",
	"janubiy afrika": "pretoriya",
	"nigeriya": "abuca",
	"egipet": "qohira"
}
# print("Davlatlar nomlari:")
# for davlat in sorted (davlatlar.keys()):
# 	print(davlat.title())
# print("Davlatlar poytaxtlari:")
# for poytaxt in sorted (davlatlar.values()):
# 	print(poytaxt.title())

# davlat = input("Davlat nomini kiriting:")
# if davlat.lower() in davlatlar:
# 		print(f"{davlat.title()} poytaxti: {davlatlar[davlat.lower()].title()}")
# else:
# 		print(f"Kechirasiz, bizda {davlat.title()} haqida ma'lumot yo'q.")

menu = {
    "osh": 30000,
    "shashlik": 20000,
    "norin": 15000,
    "baliq": 25000,
    "non": 10000,
    "bodring": 20000,
    "tuxum": 15000,
    "manti": 20000,
    "qozonkabob": 30000,
    "rangi kabob": 30000,
    "salat": 15000,
    "choy": 5000,
    "sharbat": 7000,
    "limonad": 8000,
    "gazak": 10000,
    "shirinlik": 12000,
    "pitsa": 25000,
    "burger": 20000,
    "hot-dog": 15000,
    "makaron": 18000,
    "qaymoq": 12000,
}

# Foydalanuvchidan 3 ta buyurtma olish
buyurtmalar = []
for i in range(3):
    taom = input(f"{i+1}-buyurtmangizni kiriting: ").lower()
    buyurtmalar.append(taom)

# Har bir taomni tekshirish
for taom in buyurtmalar:
    if taom in menu:
        print(f"{taom.title()} narxi: {menu[taom]} so'm")
    else:
        print(f"Kechirasiz, bizda {taom} yo'q.")
