from random import randint

def coin():
    if (a := 0 if input('裏か表か: ') == '裏' else 1) == (b :=randint(0,1)):
        print("当たり！！")
    else:
        print("ハズレ〜")
        

coin()
     


