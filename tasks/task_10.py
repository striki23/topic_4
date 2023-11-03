number = input('Введите положительное трехзначное число: ')

hundreds = int(number[0])
tens = int(number[1])
units = int(number[2])

sum_digits = hundreds + tens + units

product_digits = hundreds * tens * units

print('Сумма цифр: ', sum_digits)
print('Произведение цифр: ', product_digits)
