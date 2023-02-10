# # v.1
# import modul1
# print(modul1.max1(5, 9))

# # v.2 импорт функции напрямую
# from modul1 import max1
# print(max1(5, 3))

# # v.3 импорт функции(й) напрямую незная их названий
# from modul1 import *
# print(max1(10, 6))

# v.4 импорт модуля напрямую с сокращением его названия
import modul1 as m1
print(m1.max1(10, 6))
