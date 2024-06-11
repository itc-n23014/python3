from random import randint

coin = [randint(0,1) for _ in range(1000)].count(0)
print(f"表は{coin}回出ました。")

