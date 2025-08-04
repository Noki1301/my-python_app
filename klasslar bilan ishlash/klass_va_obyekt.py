class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    # __init__ bilan bir qatorda, dedent qiling:
    def get_name(self):
        return self.ism

    def get_lastname(self):
        return self.familiya

    def get_fullname(self):
        return f"{self.ism} {self.familiya}"

    def get_age(self, yil):
        return yil - self.tyil

    def set_bosqich(self, bosqich):
        self.bosqich = bosqich

    def update_bosqich(self, bosqich):
        self.bosqich += 1

    def get_info(self):
        return f"{self.ism} {self.familiya}, {self.tyil}-yilda tug'ilgan, {self.bosqich}-bosqich talabasi."


class Fan:
    """Fan nomli klass"""

    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_students(self):
        return [talaba.get_fullname() for talaba in self.talabalar]


def see_methods(klass):
    return [
        method for method in dir(klass) if method.startswith("__") is False
    ]  # bu klassni yodingda saqlab qol juda kerakli methodlar va klasslarni ko'rishda juda katta yordam beradigan funksiya


matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon", "Valiyev", 1999)
talaba2 = Talaba("Valijon", "Aliyev", 2000)
talaba3 = Talaba("Valijon", "Aliyev", 2000)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)
