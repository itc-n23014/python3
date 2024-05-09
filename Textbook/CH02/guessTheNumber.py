from random import randint #モジュール内の関数を直接呼び出す

num = randint(1, 20)
print("数字を当ててください(1~20)")
i = 0
while i < 6 and (gn := int(input(f"{i+1}回目: "))) != num:
    print("もっと大きい数値です." if num > gn else "もっと小さい数値です.")
    i += 1

print(f"おめでとう！{i+1}回目で当てました " if i < 6 else f"残念！正解は{num}でした.")

