# Задача
# Необходиимо создать функцию, которая будет считать сумму
# всех элементов от 1 до n.
# вариант 1
# def sumNumbers(n):            # создадим функцию с аргументом n
#     summa = 0
#     for i in range(1, n + 1): # проходимся по всем элементам
#         summa += i            # при каждой итерации будем увеличивать сумму на текущее i
#     print(summa)              # вывод суммы каждой итерации

# n = int(input())              # ввод числа
# sumNumbers(n)                 # вывод итоговой суммы

# вариант 2
# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# n = int(input())
# print(sumNumbers(n))

# # вариант 3
# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# n = int(input())
# a = sumNumbers(n)
# print(a)

# # чтобы не забывать, что сколько аргументов мы передаём, столько
# # и принимаем сразу можно при создании функции записать (присвоить)
# # аргумент по умолчанию
# def sumNumbers(n, y = 'Hello'): # второму аргументу присвоени значение "Hello" по умолчанию
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# n = int(input())
# # a = sumNumbers(n)
# a = sumNumbers(n, 'qwerty')
# print(a)

# # Задача:
# # Передать функции множество букв и в итоге получить единое слово, но мы не знаем
# # сколько будет букв и не знаем сколько  надо передать аргументов.
# # Чтобы передать неизвестное количество аргументов, то в качестве
# # аргумента функции записывают аргумент со стоящим впереди знаком *.
# def sum_str(*args):   # создадим функцию, которая будет принимать наименьшее количество аргументов
#     res = ''          # создадим переменную, которая имеет тип данных строка
#     for i in args:    # пройдёмся по всем элементам переменной args
#         res += i      # при каждой итерации к переменной res будем добавлять значение переменной i
#     return res        # возвратим res
# print(sum_str('H', 'e', 'l', 'l', 'o', '!')) # вывод результата
# # print(sum_str(1, 9, 7, 4))

# # РЕКУРСИЯ
# def fib(n):               # создадим функцию
#     if n in [1, 2]:       # условие выхода (если n находится в списке,\
#         return 1          # то должна вернуться 1).
#     return fib(n - 1) + fib(n - 2) # иначе вернём рекурсию

# list1 = []                # создадим список в который будем записывать числа
# for i in range(1, 10):    # пройдёмся по списку от 1 до 9
#     list1.append(fib(i))  # при каждой итерации цикла в список буде добавлять вызов функции
# print(list1)              # выведим получившийся список

# # АЛГОРИТМЫ
# # БЫСТРАЯ сортировка (бинарный поиск)
# def quick_sort(array):        # создаём функцию в аргумент которой передаём массив
#     if len(array) <= 1:       # проверка, если длина массива меньше 1
#         return array          # то возвратим этот массив
#     else:                     # иначе
#         pivot = array[0]      # создадим переменную в которой будем сохранять 1-й элемент массива
#     less = [i for i in array[1:] if i <= pivot] # воспользуемся генератором списков. будем брать все\
#                                                 # элементы которые стоят после 1-го элемента и будем\
#                                                 # проходиться по всем элементам и добавлять только те,\
#                                                 # которые будут <= pivot
#     greater = [i for i in array[1:] if i > pivot] # создадим 2-й массив, где будем записывать те элементы,\
#                                                   # которые > pivot
#     return quick_sort(less) + [pivot] + quick_sort(greater) # возвратим вызов рекурсии
# # print(quick_sort([14, 5, 9, 6, 3, 5, 8, 7, 5, 2, 7]))
# print(quick_sort([10, 5, 2]))
# #         1-е повторение рекурсии:
# #             arry = [10, 5, 2]
# #             pivot = 10
# #             less = [5, 2]
# #             greater = []
# #             return quick_sort([5, 2]) + [10] + quick_sort([])
# #         2-е повторение рекурсии:
# #             arry = [5, 2]
# #             pivot = 5
# #             less = [2]
# #             greater = []
# #             return quick_sort([2]) + [5] + quick_sort([])
# #         3-е повторение рекурсии:
# #             arry = [2]
# #             return[2]
# #         Вывод:
# #             [2] + [5] + [10] = [2, 5, 10]

# ЗАДАЧА
# Сортировка СЛИЯНИЕМ
def merge_sort(nums):               # создадим функцию и в качестве аргумента передадим список
    if len(nums) > 1:               # проверка, когда длина списка > 1
        mid = len(nums) // 2        # создаём переменную в которой будет храниться значение середины списка
        left = nums[:mid]           # создаём 1-й список, он получается путём обращения к левой части списка
        right = nums[mid:]          # создаём 2-й список, где будет храниться правая часть списка
                                    # Эти списки постоянно будем делить до конца при помощи рекурсии
        merge_sort(left)            # вызовим и выполним функцию для левой части списка
        merge_sort(right)           # также сделаем и для правой части списка
        i = j = k = 0               # создадим переменные, которые будут равны 0

        while i < len(left) and j < len(right): # создадим цикл, в котором все элементы будут складываться\
                                                # последовательно. он будет выполняться до тех пор пока\
                                                # переменная i будет <, чем длина левой части списка и\
                                                # одновременно, пока j будет <, чем длина правой части списка
            if left[i] < right[j]:  # если элемент из левой части списка меньше, чем из правой части списка
                nums[k] = left[i]   # то в переменную k запишем значение i
                i += 1
            else:                   # иначе
                nums[k] = right[j]  # в переменную k запишем значение j
                j += 1
            k += 1                  # также при каждой итерации цикла надо увеличивать переменную k на 1
        
        while i < len(left):        # пока переменная i меньше чем длина левого списка
            nums[k] = left[i]       # элемент списка nums равен элементу леаого списка
            i += 1
            k += 1

        while j < len(right):       # пока переменная j меньше чем длина левого списка
            nums[k] = right[j]      # элемент списка nums равен элементу правого списка
            j += 1
            k += 1

list1 = [38, 27, 43, 3, 9, 82, 10]  # создаём список вручную
merge_sort(list1)                   # вызываем функцию для списка list1
print(list1)                        # выводим список list1
