from random import randint

def coin():
    count = 0
    while (count != 2):
        if (a := 0 if input('裏か表か: ') == '裏' else 1) == (b :=randint(0,1)):
            print("当たり！！")
            break
        else:
            count += 1
            print('ハズレ、もう一回頑張れ！'if count == 1 else '残念、苦手だね.') 




        

coin()
     


