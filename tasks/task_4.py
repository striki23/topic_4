num_chicken = int(input('Введите количество курочек: '))
num_cows = int(input('Введите количество коровок: '))
num_pigs = int(input('Введите количество свинок: '))

total_legs = (num_cows + num_pigs) * 4 + num_chicken * 2

print('Общее количество ног на ферме: ', total_legs)
