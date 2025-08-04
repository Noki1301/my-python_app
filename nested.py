# car0 = {
# 	"model": "Lacetti",
# 	"rang": "Oq",
# 	"yil": 2010,
# 	"narx": 8000,
# 	"km": 150000,
# 	"korobka": "mexanik"
# }
# car1 = {
# 	"model": "nexia-3",
# 	"rang": "Qora",
# 	"yil": 2019,
# 	"narx": 9000,
# 	"km": 15000,
# 	"korobka": "mexanik"
# }
# car2 = {
# 	"model": "Gentra",
# 	"rang": "Metallik",
# 	"yil": 2020,
# 	"narx": 12000,
# 	"km": 1500,
# 	"korobka": "Avtomat"
# }

# # car = car2
# # print(f"Model: {car['model'].title()}, "
# # 			f"Rangi: {car['rang']}, "
# # 			f"Yili: {car['yil']}, Narxi: {car['narx']}")

# cars = [car0, car1, car2]
# # for car in cars:
# # 	print(f"Model: {car['model'].title()}, "
# # 			f"Rangi: {car['rang']}, "
# # 			f"Yili: {car['yil']}, Narxi: {car['narx']} $")

# # print(f"{cars[0]['rang']} "
# # 			f"{cars[0]['model']}")

# malibus = []
# for n in range(10):
# 	malibu = {
# 		"model": "malibu 2",
# 		"rang": "none",
# 		"yil": 2020,
# 		"narx": "none",
# 		"km": 0,
# 		"korobka": "avtomat"
# 	}
# 	malibus.append(malibu)
# # print(malibus)

# for malibu in malibus[:3]:
# 	malibu['rang'] = 'qora'
# 	# print(malibu)

# for malibu in malibus[3:6]:
# 	malibu['rang'] = 'oq'
# 	# print(malibu)
# for malibu in malibus[6:]:
# 		malibu['rang'] = 'qizil'
# 		malibu['korobka'] = 'mexanik'
# 		# print(malibu)
# # for malibu in malibus:
# 	# print(malibu)

# for malibu in malibus:
# 		if malibu['korobka'] == 'avtomat':
# 			malibu['narx'] = 30000
# 		else:
# 			malibu['narx'] = 25000

# for malibu in malibus:
# 		print(f"{malibu['rang'].title()} "
# 			  f"{malibu['model'].title()}, "
# 			  f"Yili: {malibu['yil']}, "
# 			  f"Narxi: {malibu['narx']} $")

# dasturchilar = {
# 	"Ali":["Python", "Java"],
# 	"Vali":["PHP", "C++"],
# 	"Hasan":["JavaScript", "C#"],
# 	"Zohid":["Go", "Rust"],
# 	"Olim":["Python", "C++", "Go"],
# 	"Anvar":["JavaScript", "PHP", "Java"],
# 	"Bobur":["Java", "C#"],
# 	"Shahzod":["Python", "JavaScript", "C++"],
# 	"Madina":["Java", "PHP", "C#"],
# 	"Nilufar":["Go", "Rust", "Python"],
# 	"Yulduz":["JavaScript", "C++", "PHP"]
# }
# for ismlar,tillar in dasturchilar.items():
# 	print(f"\n{ismlar.title()} quyidagi dasturlash tillarini biladi:")
# 	for til in tillar:
# 		print(f"{til.upper()} ", end="")

# hamkasblar = {
# 	"ali":{
# 	"ism": "Ali",
# 		"familiya": "Valiyev",
# 		"yosh": 25,
# 		"kasb": "Dasturchi",
# 		"tillar": ["Python", "Java"]
# 	}
# 	,"vali":{
# 	"ism": "Vali",
# 		"familiya": "Sultonov",
# 		"yosh": 30,
# 		"kasb": "Dasturchi",
# 		"tillar": ["PHP", "C++"]
# 	},
# 	"hasan":{
# 	"ism": "Hasan",
# 		"familiya": "Xolmirzayev",
# 		"yosh": 28,
# 		"kasb": "Dasturchi",
# 		"tillar": ["JavaScript", "C#"]
# 	}
# }
# for ism,info in hamkasblar.items():
# 	print(f"\n{ism.title()} {info['familiya'].title()}, "
# 			 f"{info['yosh']} yoshda",
# 			 f"uning kasbi {info['kasb']}.\n",
# 			 f"quyidagi dasturlash tillarini biladi:")
# 	for til in info['tillar']:
# 		print(f"{til.upper()} ", end="")

# Amaliyot: 1-masala 

mashxurlar = {
		"Bill":{
			"ism": "Bill",
			"familiya": "Geyts",
			"yosh": 68,
			"kasb": "Dasturchi",
			"asarlari": ["Windows", "Microsoft Office"],
			"tillar": ["Python", "Java"]
		}
		,"Mark":{
			"ism": "Mark",
			"familiya": "Zukerberg",
			"yosh": 40,
			"kasb": "Dasturchi",
			"asarlari": ["Facebook", "Instagram"],
			"tillar": ["PHP", "C++"]
		},
		"Elon":{
			"ism": "Elon",
			"familiya": "Musk",
			"yosh": 50,
			"kasb": "Dasturchi",
			"asarlari": ["Tesla", "SpaceX"],
			"tillar": ["JavaScript", "C#"]
		},
		"Shavkat":{
			"ism": "Shavkat",
			"familiya": "Mirziyoyev",
			"yosh": 65,
			"kasb": "Prezident",
			"asarlari": ["O'zbekiston", "Yangi O'zbekiston"],
			"tillar": ["O'zbek", "Rus", "Ingliz"]
		},
	}
shaxslar = ["Bill", "Mark", "Elon", "Shavkat"]
for shaxs in shaxslar:
	if shaxs in mashxurlar:
		info = mashxurlar[shaxs]
		print(f"\n{info['ism']} {info['familiya']}, "
				f"{info['yosh']} yoshda, "
				f"Uning kasbi {info['kasb']}.\n"
				f"Uning asarlari:")
		for asar in info['asarlari']:
			print(f"{asar} ", end="")
		print("\nU quyidagi dasturlash tillarini biladi:")
		for til in info['tillar']:
			print(f"{til.upper()} ", end="")
	else:
		print(f"Kechirasiz, {shaxs} haqida ma'lumot yo'q.")

# Amaliyot: 3-masala
# malumotlar = {"ism": input("Ismingiz nima?\n>>>"),
# 		"familiya": input("Familiyangiz nima?\n>>>"),
# 		"yosh": int(input("Yoshingiz nechida?\n>>>")),
# 		"kasb": input("Kasbingiz nima?\n>>>"),
# 		"kinolar": []
# 	}
# for n in range(3):
# 	malumotlar["kinolar"].append({
# 		"nomi": input(f"{n+1}-chi sevimli kinongiz nima?\n>>>")
# 	})
# print(f"\n{malumotlar['ism'].title()} {malumotlar['familiya'].title()}, "
# 		f"{malumotlar['yosh']} yoshda, "
# 		f"Uning kasbi {malumotlar['kasb']}.\n"
# 		f"Uning sevimli kinolari:")
# for kino in malumotlar['kinolar']:
# 	print(f"{kino['nomi'].title()} ", end="")

davlatlar = {
	"uzbekistan": {
		"poytaxt": "toshkent",
		"hudud": 448978,
		"aholi": 35000000,
		"pul birligi": "so'm",
		"president": "Shavkat Mirziyoyev"
	},
	"qozog'iston": {
		"poytaxt": "astana",
		"hudud": 2724900,
		"aholi": 19000000,
		"pul birligi": "tenge",
		"president": "Qasym-Jomart Toqayev"
	},
	"rossiya": {
		"poytaxt": "moskva",
		"hudud": 17098242,
		"aholi": 145912025,
		"pul birligi": "rubl",
		"president": "Vladimir Putin"
	},
	"qirg'iziston": {
		"poytaxt": "bishkek",
		"hudud": 199951,
		"aholi": 6500000,
		"pul birligi": "som",
		"president": "Sadir Japarov"
	}
}
# Amaliyot: 4-masala
# for davlat,info in davlatlar.items():
# 	print(f"{davlat.title()} poytaxti {info['poytaxt'].title()}, "
# 			f"Aholi soni {info['aholi']} mln inson, Pul birligi {info['pul birligi']}, "
# 			f"Prezidenti {info['president']}, "
# 			f"Hududi {info['hudud']} kv.km.")

# Amaliyot: 5-masala

# sorov = input("Qaysi davlat haqida ma'lumot olishni xohlaysiz?\n>>> ").lower()
# if sorov in davlatlar.keys():
# 	print(f"{sorov.title()} poytaxti {davlatlar[sorov]['poytaxt'].title()}, "
# 			f"Aholi soni {davlatlar[sorov]['aholi']} mln inson, Pul birligi {davlatlar[sorov]['pul birligi']}, "
# 			f"Prezidenti {davlatlar[sorov]['president']}, "
# 			f"Hududi {davlatlar[sorov]['hudud']} kv.km.")
# else:
# 	print("Kechirasiz, bizda bunday davlat haqida ma'lumot yo'q.")