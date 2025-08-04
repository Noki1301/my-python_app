def avto_info(kompaniya, model, rangi, korobka, yili, narhi = None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto
def avto_kirit():
	print("Onlayn bozordagi avtomobillar ruyxatini shakllantiramiz:")
	avtolar = []
	while True:
			print("\nQuyidagi ma'lumotlarni kiriting:", end=' ')
			kompaniya = input("Ishlab chiqaruvchi: ")
			model = input("Modeli: ")
			rangi = input("Rangi: ")
			korobka = input("Korobka: ")
			yili = input("Ishlab chiqarilgan yili: ")
			narhi = input("Narhi: ")
			avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
			javob = input("Yana avto qo'shasizmi? (ha/yo'q)")
			if javob.lower() != 'ha':
					break
def avto_chiqar(avtolar):    
			print("\nOnlayn bozordagi avtomobillar:")
			for avto in avtolar:
					if avto["narh"]:
							narh = avto["narh"]
					else:
							narh = "Noma'lum"
					print(f"{avto['rang'].title()} {avto['kompaniya'].title()} {avto['model'].title()} "
								f"{avto['yil']}-yil, {avto['korobka'].title()} korobka, narhi: {narh} $")
