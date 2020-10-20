def fight():
    my_hp = 1200
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        if my_hp > enemy_hp:
            print("I win")
            break
        elif my_hp < enemy_hp:
            print("I fail, the enemy win")
            break


fight()
