class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

        def get_info(self):
            """Shaxs haqida ma'lumot"""
            info = f"{self.ism} {self.familiya}. "
            info += f"Passport:{self.passport}, {self.tyil}-yilda tug'ilgan"
            return info

        def get_age(self, yil):
            """Shaxsning yoshini qaytaruvchi metod"""
            return yil - self.tyil


class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, idraqam, bosqich, manzil):
        """Talaba xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = bosqich
        self.manzil = manzil

    def get_id(self):
        return self.idraqam

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"ID raqami: {self.idraqam}, {self.bosqich}-bosqich"
        return info

    def get_bosqich(self):
        return self.bosqich
class Manzil:
    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.uy}-uy, {self.kocha} ko'chasi, {self.tuman} tumani, {self.viloyat} viloyati"
        return manzil

talaba1_manzil = Manzil(12, "Ulug'bek", "Qarshi", "Andijon")
talaba1 = Talaba("Alijon", "Valiyev", "FA112299", 2000, "123456789", 3, talaba1_manzil)
#  VORIS likning afzalligi shundan iboratki biz agar super klassda biror xususiyat yozsak uni qolgasn voris klasslarda ham qayta qayta ishlatsa bo'ladi
# POLIMORFIZM ning afzalligi shundan iboratki, agar super klass ichidagi biror bir method biz kutgan natijani qaytarmayotgan bo'lsa biz voris klass ichida qaytadan o'zimizga moslab yozishimiz mumkin 
