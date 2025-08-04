# ism = "Sardor"
# print(f"Salom, {ism}!")

# ism = input("Ismingiz nima?\n>>>")
# print(f"Salom, {ism.title()}!")

# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor"
# viloyat="Samarqand"
# print(f"{kocha} ko\'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

print("Iltimos, quyidagi ma'lumotlarni kiriting:")
kocha = input("Ko'changiz: ")
mahalla = input("Mahallangiz: ")
tuman = input("Tumaningiz: ")
viloyat = input("Viloyatingiz: ")
# print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + \
#       tuman + " tumani,\n" + viloyat + " viloyati")


manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())
print(manzil.swapcase())