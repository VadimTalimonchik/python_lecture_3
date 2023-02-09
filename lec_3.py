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

# List Comprehension
# # как делали раньше:
# list = []
# for i in range(1, 101):
#     if(i % 2 == 0):
#         list.append(i)
# print(list)

# # используя List Comprehension
# # без условия проверки на чётность
# list = [i for i in range(1, 101)]
# print(list)

# # с условием проверки на чётность
# list = [i for i in range(1, 101) if i % 2 == 0]
# print(list)

# # создание пары каждого из чисел (подключение кортежей)
# list = [(i, i) for i in range(1, 101) if i % 2 == 0]
# print(list)

# # обработка данных
# def f(x):
#     return x ** 3
# list = [f(i) for i in range(1, 101) if i % 2 == 0]
# print(list)

# # обработка данных и подключение кортежей
# def f(x):
#     return x ** 3
# list = [(i, f(i)) for i in range(1, 101) if i % 2 == 0]
# print(list)

# Задача:
# В файле хранятся числа, нужно выбрать чётные и составить список пар (число; квадрат числа).
# Ввод:
# 1 2 3 8 15 23 38
# Вывод:
# [(2, 4), (8, 64), (38, 1444)]
# # как делали раньше:
# path = 'file.txt' # есть путь к файлу
# f = open(path, 'r') # связываем файловую переменную с файлом на диске
# data = f.read() + ' ' # читаем файл (искусственный приём: считываем всё,
#                       # что есть и искуственно добавляем пробел)
# f.close() # закрываем файл

# numbers = []                              # создаём пустой список, который заполним далее\
# while data != '':                         # пробегаемся по всей строке и делаем проверку\
#                                           # "пока строка не пустая"
#     space_pos = data.index(' ')           # находим первую позицию пробела
#     numbers.append(int(data[:space_pos])) # берём всё, что находится от первого символа\
#                                           # до позиции первого пробела, превратим это в\
#                                           # число и добавим в список чисел
#     data = data[space_pos + 1:]           # обновляем строку с учётом того, что теперь то, что было\
#                                           # сюда добавлено, уже не надо будет сдесь использовать

# out = []                                  # создаём новый список
# for e in numbers:                         # пробегаемся по исходному списку
#     if not e % 2:                         # проверяем условие того, что число действительно\
#                                           # является чётным
#         out.append((e, e ** 2))           # добавляем в новый список картежи, где в качестве 1-ой\
#                                           # координаты выступает само число, а в качестве 2-ой -\
#                                           # квадрат эього числа
# print(out)                                # вывод результата в консоль

# новый способ
def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
res = where(lambda x: not x % 2, res)
res = select(lambda x: (x, x ** 2), res)
print(res)
