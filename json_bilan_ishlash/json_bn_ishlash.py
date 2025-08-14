import json

# bemor = {
#     "ism": "Abdulloh",
#     "familya": "Abdullayev",
#     "t_yil": 2002,
#     "m_t_yil": 2022,
#     "telefon": "998941234567",
#     "yoshi": 20,
#     "allergiya": None,
#     "dorilar": [
#         {"nomi": "Penicillin", "miqdori": 1},
#         {"nomi": "Aspirin", "miqdori": 2},
#         {"nomi": "Ibuprofen", "miqdori": 1},
#         {"nomi": "Paracetamol", "miqdori": 2},
#         {"nomi": "Cefalexin", "miqdori": 1},
#         {"nomi": "Amoxicillin", "miqdori": 1},
#     ],
# }

# bemor_json = json.dumps(
#     bemor, indent=4, ensure_ascii=False, sort_keys=True, separators=(",", ":")
# )
# print(bemor_json)

# with open("bemor_json", "w") as f:
#     # json.dump(bemor, f)
#     bemor = json.loads(bemor_json)
#     print(type(bemor))

# # Amaliyot 1 - masala
# data = {"Model": "Malibu", "Rang": "Qora", "Yil": 2020, "Narh": 40000}

# with open("data.json", "w") as f:
#     json.dump(data, f)

# with open("data.json", "r") as f:
#     data = json.load(f)
#     print(data)

# # Amaliyot 2 - masala
# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# talaba = json.loads(talaba_json)
# print(f"{talaba['ism'].title()} {talaba['familiya'].title()}")

# # Amaliyot 3 - masala
# talaba1 = {"ism": "Husan", "familiya": "Husanov", "tyil": 2000}
# talaba1_json = json.dumps(
#     talaba1, indent=4, ensure_ascii=False, sort_keys=True, separators=(",", ":")
# )

# # Ism-familiyani dict’dan o‘qing:
# print(f"{talaba1['ism'].title()} {talaba1['familiya'].title()}")

# # JSON matnini alohida ko‘rsating (ixtiyoriy):
# print(talaba1_json)

# mashina = {"model": "Malibu", "rang": "Qora", "yil": 2020, "narh": 40000}
# mashina_json = json.dumps(
#     mashina, indent=4, ensure_ascii=False, sort_keys=True, separators=(",", ":")
# )
# print(mashina_json)

# Amaliyot 4 - masala
# import json

# with open("json_bilan_ishlash/students.json") as f:
#     data = json.load(f)

# for item in data["student"]:
#     print(f"{item['name']} {item['lastname']}." f" Faculty of {item['faculty']} ")


# Amaliyot 5 - masala
with open("noki.json") as f:
    wiki = json.load(f)

print(wiki["query"]["pages"]["13801"]["title"])
print(wiki["query"]["pages"]["13801"]["extract"])
