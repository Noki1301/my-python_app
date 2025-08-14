# INKOPSULIYATSIYA deb biror bir obyekt xususiyatini yashirin qilish yani tashqaridan murojat qilishni yopish
from uuid import uuid4


class Avto:
    """Avto klassi"""

    __num_avto = 0  # avto klassining obyektlar soni

    def __init__(self, make, model, rang, yil, narh, km=0):
        """Avto klassining hususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km  # private yani inkapsulyatsiya misol
        self.__id = uuid4()
        Avto.__num_avto += 1

    def __repr__(self): #repr metodi  representation degani va u universal
        return f"Avto('{self.make}', '{self.model}', '{self.rang}', {self.yil}, {self.narh}, {self.__km})"

    def __eq__(self, y):
        return self.narh == y.narh

    def __lt__(self, y):
        return self.narh < y.narh
    def __le__(self, y):
        return self.narh <= y.narh


    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:
            print("Mashina km ni kamaytirib bo'lmaydi.")


avto1 = Avto("GM", "Malibu", "qora", 2018, 20000)
avto2 = Avto("GM", "Malibu", "qora", 2018, 20000)
avto3 = Avto("GM", "Malibu", "qora", 2018, 20000)
avto4 = Avto("GM", "Malibu", "qora", 2018, 20000)
avto5 = Avto("GM", "Malibu", "qora", 2018, 20000)
avto6 = Avto("GM", "Malibu", "qora", 2018, 20000)
# print(Avto.get_num_avto())
