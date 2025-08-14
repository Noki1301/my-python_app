# Amaliyot 1 - masala
# with open("data/file.txt", "r") as file:
#     print(file.read())

# Amaliyot 2 - masala
# with open("data/pi_million_digits.txt", "r") as file:
# 	pi = file.read()
# 	def pi_contains_date(path, day, month, year):
# 		with open(path, "r", encoding="utf-8") as f:
# 			pi = f.read()
# 			pi = "".join(ch for ch in pi if ch.isdigit())
# 			date_seq = f"{day:02d}{month:02d}{year:04d}"
# 			if date_seq in pi:
# 				idx = pi.find(date_seq)
# 				print(f"{date_seq} topildi! (indeks: {idx})")
# 				return True, idx
# 			else:
# 				print(f"{date_seq} topilmadi.")
# 				return False, -1

# pi_contains_date("data/pi_million_digits.txt", 13, 1, 1996)

# Amaliyot 3 - masala
# import pickle

# # Manba faylni binar rejimda ochamiz, so'ng UTF-8 ga dekod qilamiz
# with open("data/pi_million_digits.txt", "rb") as f:
#     text = f.read().decode("utf-8", errors="ignore")

# # Matndan faqat raqamlar va birinchi nuqtani qoldiramiz: "3.1415..."
# num_chars = []
# dot_used = False
# for ch in text:
#     if ch.isdigit():
#         num_chars.append(ch)
#     elif ch == "." and not dot_used:
#         num_chars.append(".")
#         dot_used = True

# num_str = "".join(num_chars)  # "3.1415926..."
# pi_float = float(num_str)  # >>> faqat ~16 ta raqam aniq bo'ladi!

# # Pickle'ga saqlaymiz
# with open("data/pi_float.pkl", "wb") as f:
#     pickle.dump(pi_float, f)

# # (ixtiyoriy) Tekshirish uchun qayta yuklab ko'ramiz
# with open("data/pi_float.pkl", "rb") as f:
#     loaded = pickle.load(f)
#     print(repr(loaded))

# Amaliyot 4 - masala
from pathlib import Path

# Skript joylashgan papkaga nisbatan yo‘l (REPL’da esa joriy papka)
BASE_DIR = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
FILE_PATH = BASE_DIR / "data" / "malumotlar.txt"

# data/ papkasini yaratib qo'yamiz (bo'lmasa)
FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

with FILE_PATH.open("a", encoding="utf-8") as f:
    while True:
        print("\nYangi yozuv (bo'sh ism — tugatish)")
        ism = input("Ism: ").strip()
        if ism == "":
            break
        tel = input("Telefon: ").strip()
        email = input("Email: ").strip()

        f.write(f"Ism: {ism}\n")
        f.write(f"Tel: {tel}\n")
        f.write(f"Email: {email}\n")
        f.write("---\n")
        print("✅ Saqlandi.")
