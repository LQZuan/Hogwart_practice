import random


def fight(enemy_hp, enemy_power):
    my_hp = 1200
    my_power = 200
    print("The enemy hp: ", enemy_hp)
    print(f"The enemy power: {enemy_power}")

    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        if my_hp > enemy_hp:
            print(f"My rest hp: {my_hp}")
            print(f"Enemy rest hp: {my_hp}")
            print("I win")
            break
        elif my_hp < enemy_hp:
            print("I fail, the enemy win")
            print(f"My rest hp: {my_hp}")
            print(f"Enemy rest hp: {my_hp}")
            break




if __name__ == "__main__":
    hp = [x for x in range(990, 1010)]
    print(hp)
    print(type(hp))
    enemy_hp = random.choice(hp)
    enemy_power = random.randint(190, 200)
    fight(enemy_hp, enemy_power)