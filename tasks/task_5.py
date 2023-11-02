wins = int(input('Введите количество побед: '))  # Ваш код
draws = int(input('Введите количество ничейных игр: '))  # Ваш код
losses = int(input('Введите количество поражений: '))  # Ваш код

total_points = wins * 3 + draws * 1 + losses * 0

print('Общее количество очков: ', total_points)
