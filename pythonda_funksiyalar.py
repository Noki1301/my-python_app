# import math 
# uzulik = lambda pi,r : 2 * pi * r
# print(uzulik(math.pi, 10))

# kvadrat = lambda x, y : x ** y
# print(kvadrat(3, 2))
 
# def daraja(n):
#     return lambda x : x ** n
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kub(3)} ga, kubi {kvadrat(3)} ga teng")

# from math import sqrt
# sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
# print(ildizlar)

# def daraja2(x):
#     return x*x
# print(list(map(daraja2, sonlar)))

# kvadratlar = list(map(lambda x: x*x, sonlar))
# print(kvadratlar)

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# a_plus_b = list(map(lambda x, y: x+y, a, b))
# print(a_plus_b)

# ismlar = ['hasan', 'husan', 'olim', 'botir']
# print(list(map(lambda matn: matn.upper(), ismlar)))
import random as r
sonlar = r.sample(range(100),10)
# print(sonlar)
# def juftmi(x):
# 		return x % 2 == 0
# juft_sonlar = list(filter(juftmi, sonlar))
# print(juft_sonlar)
# juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
# print(juft_sonlar)

mevalar = ['olma', 'anor', 'anjir', 'shaftoli', 'o\'rik', 'tarvuz', 'qovun', 'banan']
# harf = 'o'
# mevalar_b = list(filter(lambda meva: meva.startswith(harf), mevalar))
# print(f"{harf} boshlanayotgan mevalar: {mevalar_b}")
mevalar2 = list(filter(lambda meva: len(meva) <= 5, mevalar))
# print(mevalar2)

list(filter(lambda meva: meva.startswith('a') and meva.endswith('r'), mevalar))
print(mevalar)
