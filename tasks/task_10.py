number = input('Введите положительное трехзначное число: ')

hundreds = int(number[0])
tens = int(number[1])
units = int(number[2])

# Еще вариант без использования индекса строк:

# hundreds = int(number)//100
# tens = (int(number) - int(str(hundreds)+'00'))//10
# units = int(number) - int(str(hundreds) + str(tens) + '0')

sum_digits = hundreds + tens + units
product_digits = hundreds * tens * units

print('Сумма цифр: ', sum_digits)
print('Произведение цифр: ', product_digits)
