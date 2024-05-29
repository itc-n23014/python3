import re

def date_detecter(s):
    regex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
    list = [0,0,0]
    d,m,y = map(int,[i for i  in regex.findall(s)][0])
    list[2] = 0 if not 999 < y < 3000 else 1
    list[1] = 1 if 0 < m < 13 else 0
    list[0] = 1 if m in [1,3,5,7,8,10,12] and d < 32 or m in [3,4,6,9,11] and 0 < 31 or m == 2 and d < 29 else 0
    return all(list)


a = input("dd/mm/yyyy フォーマットで日付を入力: ")
print(date_detecter(a))
    
