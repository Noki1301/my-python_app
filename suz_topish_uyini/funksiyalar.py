import random
from uzwords import words

def get_word():
    """So'z royxatdan tasodifiy so'z olib, ichida '-' yoki ' ' bo'lsa qayta tanlaymiz."""
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def display_word(user_letters: set, word: str) -> str:
    """Topilgan harflar ko'rsatiladi, qolganlari tire (“-”) bilan yashiriladi."""
    return ''.join(letter if letter in user_letters else '-' for letter in word)

def play():
    word = get_word()
    word_letters = set(word)      # hali topilmagan harflar
    user_letters = set()          # foydalanuvchi kiritgan xarflar
    attempts = 0

    print(f"Men {len(word)} xonali so'z o'yladim. Topa olasizmi?")

    while word_letters:
        # so'zni ko'rsatish va avvalgi kiritilgan xarflar
        print(display_word(user_letters, word))
        print(f"Shu vaqtgachaga kiritgan xarflaringiz: {' '.join(sorted(user_letters))}")

        letter = input("Harf kiriting: ").strip().upper()
        # faqat bittadan harf ekanligini tekshiramiz
        if len(letter) != 1 or not letter.isalpha():
            print("Iltimos, faqat bitta lotin harf kiriting.")
            continue
        # takror kiritmaslik
        if letter in user_letters:
            print("Bu harfni avval kiritgansiz.")
            continue

        user_letters.add(letter)
        attempts += 1

        if letter in word_letters:
            word_letters.remove(letter)
            print(f"{letter} harfi to'g'ri!")
        else:
            print("Bunday harf yo'q.")

    # tsikl tugagach (so'z to'liq topilgach) tabrik xabari
    print(f"Tabriklayman, {word} so'zini {attempts} ta urinishda topdingiz!")
