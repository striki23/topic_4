number = int(input('Введите положительное трехзначное число: '))

number_3 = number % 10
number_2 = number // 10 % 10
number_1 = number // 100

sum_digits = number_1 + number_2 + number_3
product_digits = number_1 * number_2 * number_3

print('Сумма цифр:', sum_digits)
print('Произведение цифр:', product_digits)
