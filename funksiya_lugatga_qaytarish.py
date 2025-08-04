# def bahola(ismlar):
# 	baholar = {}
# 	while ismlar:
# 		ism = ismlar.pop()
# 		baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
# 		baholar[ism] = int(baho)
# 	return baholar
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])
# print(baholar)
# print(talabalar)

# Amaliyot 1-2 masalalariga javob 

# def matnli_ruyhat(matn):
# 	"""
# 	Matnli ruyhatni qabul qilib, har bir so'zning bosh harfini katta harfga o'zgartirib qaytaruvchi funksiya.
# 	"""
# 	ruyhat = []
# 	for soz in matn:
# 		ruyhat.append(soz.title())
# 	return ruyhat
# matn = ['ali', 'vali', 'hasan', 'husan']
# print(matnli_ruyhat(matn))
# print(matn)

# Amaliyot 3 masalaga javob 

talabalar = ['ali', 'vali', 'hasan', 'husan']

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
        
baholar = bahola(talabalar)
print(baholar)
print(talabalar)