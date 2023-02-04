def choose_coffee(*preference):
    global ingredients
    for pr in preference:
        if pr == 'Эспрессо':
            if ingredients[0] >= 1:
                ingredients[0] -= 1
                return pr
        if pr == 'Капучино':
            if ingredients[0] >= 1 and ingredients[1] >= 3:
                ingredients[0] -= 1
                ingredients[1] -= 3
                return pr
        if pr == 'Маккиато':
            if ingredients[0] >= 2 and ingredients[1] >= 1:
                ingredients[0] -= 2
                ingredients[1] -= 1
                return pref
        if pr == 'Кофе по-венски':
            if ingredients[0] >= 1 and ingredients[2] >= 2:
                ingredients[0] -= 1
                ingredients[2] -= 2
                return pr
        if pr == 'Латте Маккиато':
            if ingredients[0] >= 1 and ingredients[1] >= 2 and ingredients[2] >= 1:
                ingredients[0] -= 1
                ingredients[1] -= 2
                ingredients[2] -= 1
                return pr
        if pr == 'Кон Панна':
            if ingredients[0] >= 1 and ingredients[2] >= 1:
                ingredients[0] -= 1
                ingredients[2] -= 1
                return pr
    return 'К сожалению, не можем предложить Вам напиток'

ingredients = [2, 1, 0]
print(choose_coffee('Капучино','Макиато','Эспрессо'))