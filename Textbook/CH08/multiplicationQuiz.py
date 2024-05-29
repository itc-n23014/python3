import pyinputplus as p
from random import randint
import time

questions = [f"{a}*{b}=" for a, b in [(randint(0, 9), randint(0, 9)) for _ in range(10)]]

for q in questions:
    ans = eval(q[:-1])
    try:
        u_ans = p.inputInt(q, allowRegexes=[f'^{ans}$','正解！'],
                              blockRegexes=[('.*', '不正解!')],
                              timeout=8, limit=3)
    except p.TimeoutException:
        print("時間切れ!")
    except p.RetryLimitException:
        print("回数制限超え！")
    else:
        print("正解！")
        time.sleep(1)

