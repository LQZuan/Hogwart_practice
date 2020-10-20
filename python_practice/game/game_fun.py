# 引入random包
import random


def fight(enemy_hp, enemy_power):
    # 定义变量
    my_hp = 1200
    my_power = 200
    # 打印
    print("The enemy hp: ", enemy_hp)
    print(f"The enemy power: {enemy_power}")

    # while循环运算游戏规则
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        # 判断是否符合条件，并处理符合条件后跳出循环
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


"""
下面if __name__ == "__main__":语句，
在本模块中使用是，下面的代码块可以被执行
如果通过import调用这个模块，则不执行
"""
if __name__ == "__main__":
    # 列表推导式获取hp
    hp = [x for x in range(990, 1010)]
    print(hp)
    print(type(hp))
    # random.choice从list中获取变量值
    enemy_hp1 = random.choice(hp)
    # random.randint获取随机整数
    enemy_power1 = random.randint(190, 200)
    # 调用，并给函数传参
    fight(enemy_hp1, enemy_power1)
