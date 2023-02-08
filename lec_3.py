# АНОНИМНЫЕ, lambda ФУНКЦИИ

# def f(x):
#     return x**2
# print(type(f))
# print(f(2))

# g = f
# print(type(g))
# print(f(4))
# print(g(4))

# # пример применения
# def calc1(x):
#     return x + 10
# # print(calc1(10))

# def calc2(x):
#     return x * 10
# # print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 20)
# math(calc1, 20)

# # таже логика для функции с 2-мя аргументами
# def sum(x, y):
#     return x + y

# def mylt(x, y):
#     return x * y

# def calc(op, a, b):
#     print(op(a, b)) # return op(a, b)

# calc(mylt, 4, 5)

# # шаг 1 - избавляемся от написания функции
# # def sum(x, y):
# #     return x + y
# sum = lambda x, y: x + y # описание lambda с присвоение результата переменной

# def mylt(x, y):
#     return x * y

# def calc(op, a, b):
#     print(op(a, b))

# calc(sum, 4, 5)

# шаг 2 - избавляемся от перемееной sum пробрасывая lambda в качестве функцуии
# def sum(x, y):
#     return x + y
# sum = lambda x, y: x + y

# def mylt(x, y):
#     return x * y

# def calc(op, a, b):
#     print(op(a, b))

# calc(lambda x, y: x + y, 4, 5)
# calc(lambda x, y: x * y, 4, 5)

# 