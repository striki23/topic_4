interval = int(input('Введите величину временного интервала в минутах: '))

hours = interval // 60
minutes = interval % 60

print(f'Результат: {hours} часа {minutes} минут')
