# вариант 1
# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     print(summa)

# n = int(input())
# sumNumbers(n)

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

# # в
# def sumNumbers(n, y = 'Hello'):
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
# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res
# print(sum_str('H', 'e', 'l', 'l', 'o', '!'))
# # print(sum_str(1, 9, 7, 4))

# # РЕКУРСИЯ
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# list1 = []
# for i in range(1, 10):
#     list1.append(fib(i))
# print(list1)

# # АЛГОРИТМЫ
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
# # print(quick_sort([14, 5, 9, 6, 3, 5, 8, 7, 5, 2, 7]))
# print(quick_sort([10, 5, 2]))

# ЗАДАЧА
# Сортировка СЛИЯНИЕМ
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [38, 27, 43, 3, 9, 82, 10]
merge_sort(list1)
print(list1)
  