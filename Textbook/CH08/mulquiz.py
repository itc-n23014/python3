from random import randint
import time

questions = [f"{a}*{b}=" for a, b in [(randint(0, 9), randint(0, 9)) for _ in range(10)]]

for q in questions:
    ans,s_time = eval(q[:-1]),time.time()
    for _ in range(3):
        try:
            u_ans = int(input(f'{q}'))
        except:
            print("整数を入力してください.")
        if (p_time := time.time() - s_time) >= 8:
            print("時間切れ")
            break
        if ans == u_ans:
            print("正解")
            time.sleep(1)
            break
        else:
            print("不正解")

