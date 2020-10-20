def fight():
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power

    # if my_final_hp > enemy_hp:
    #     print("I win")
    # elif my_final_hp < enemy_final_hp:
    #     print("I fail, the enemy win")
    # else:
    #     print("DRAW")

    # 三目运算
    print("I win") if my_final_hp > enemy_hp else print("I fail")


fight()

