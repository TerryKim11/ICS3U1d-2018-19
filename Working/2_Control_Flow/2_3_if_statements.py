def caught_speeding(speed, is_birthday):
    if is_birthday:
        bonus = 5
    else:
        bonus = 0

    if speed <= 60 + bonus:
        print(0)
    elif 61 <= speed <= 80 + bonus:
        print(1)
    else:
        print(2)


