import pyinputplus as p
from random import randint
import time

questions = [f"{a}*{b}=" for a, b in [(randint(0, 9), randint(0, 9)) for _ in range(10)]]

for q in questions:
    ans = eval(q[:-1])
    try:
        for _ in range(3):
            u_ans = p.inputInt(f'{q}', timeout=8)
            if ans == u_ans:
                print("正解")
                time.sleep(1)
                break
            else:
                print("不正解")
    except p.TimeoutException:
        print("時間切れ!")

