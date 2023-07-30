# # Задача 22.
import random


# def get_random_number_list() -> list:
#     list_1 = []
#     range_min = int(input('Введите минимальное число в диапазоне '))
#     range_max = int(input('Введите максимальное число в диапазоне '))
#     amount = int(input('Введите количество цифр в списке '))
#     for i in range(amount):
#         list_1.append(random.randint(range_min, range_max))
#     return list_1
#
#
# def unite_two_lists_get_unique_and_sorted(list_1: list, list_2: list, ) -> list:
#     list_unite = list_1 + list_2
#     set_1 = set(list_unite)
#     list_unite = list(set_1)
#     list_unite.sort()
#     return list_unite
#
#
# list_1 = get_random_number_list()
# list_2 = get_random_number_list()
# list_3 = unite_two_lists_get_unique_and_sorted(list_1, list_2)
# print(list_1)
# print(list_2)
# print(list_3)

# # Задача № 24
# def bush_with_berries_max(number_of_pieces: int, number_of_berries_min: int, number_of_berries_max: int) -> int:
#     list_1 = []
#     list_2 = []
#     k = 0
#     for i in range(number_of_pieces):
#         list_1.append(random.randint(number_of_berries_min, number_of_berries_max))
#     print(list_1)
#     for _ in range(len(list_1)):
#         if k + 1 != len(list_1):
#             res = list_1[k - 1] + list_1[k] + list_1[k + 1]
#             k = k + 1
#         else:
#             res = list_1[-2] + list_1[-1] + list_1[0]
#         list_2.append(res)
#     print(list_2)
#     return list_2.index(max(list_2))
#
#
# number_of_pieces = int(input('Введите количество кустов '))
# number_of_berries_min = int(input('Введите минимальное количество ягод на кусте '))
# number_of_berries_max = int(input('Введите максимальное количество ягод на кусте '))
# print(f'Максимальное количество ягод можно собрать если поставить напротив {bush_with_berries_max(number_of_pieces, number_of_berries_min, number_of_berries_max)} куста')

# задача 1 необязательная.


# def input_two_or_eight() -> int:
#     while True:
#         digit = input('Введите 2 или 8 для перевода чисел в соответствующую систему ')
#         if digit in ['2', '8']:
#             return int(digit)
#         else:
#             print('Повторите ввод')
#
#
# def transfer_to_the_system_two_or_eight(number_in_ten_system: int, number_system: int) -> str:
#     list_1 = []
#     if number_system != 2 or number_system != 8:
#         contr_number = number_system
#         if number_in_ten_system < number_system:
#             list_1.append(number_in_ten_system)
#         else:
#             while number_system <= contr_number:
#                 contr_number = number_in_ten_system // number_system
#                 num1 = number_in_ten_system % number_system
#                 list_1.append(num1)
#                 number_in_ten_system = contr_number
#             list_1.append(contr_number)
#         list_1 = list_1[::-1]
#         s = ''.join(str(i) for i in list_1)
#         return s
#     else:
#         s = 'Ввели не корректные данные'
#         return s
#
#
# def concatenation_str(num_system: int, digits: str) -> str:
#     if num_system == 2:
#         result = '0b' + digits
#         return result
#     elif num_system == 8:
#         result = '0o' + digits
#         return result
#     else:
#         return 'провал'
#
#
# number_in_ten_system = int(input('Введите число в десятичной системе '))
# number_system = input_two_or_eight()
# num = transfer_to_the_system_two_or_eight(number_in_ten_system, number_system)
# print(concatenation_str(number_system, num))
# print(bin(number_in_ten_system))
# print(oct(number_in_ten_system))