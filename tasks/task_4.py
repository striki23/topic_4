num_chicken = int(input('Введите количество курочек: '))  # Ваш код
num_cows = int(input('Введите количество коровок: '))  # Ваш код
num_pigs = int(input('Введите количество свинок: '))  # Ваш код

total_legs = (num_cows + num_pigs) * 4 + num_chicken * 2

print('Общее количество ног на ферме: ', total_legs)
