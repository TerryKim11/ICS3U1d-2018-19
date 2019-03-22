def squirrel_play(temp, is_summer):
    if is_summer and 60 <= temp <= 100:
        print(True)
    elif 60 <= temp <= 90:
        print(True)
    else:
        print(False)

squirrel_play(70, False)
squirrel_play(95, False)
squirrel_play(95, True)