import re

def strip_func(s,c):
    return re.sub(fr'^[{c}]+|[{c}]+$','',s)


text = input('(文字列):(削除文字)\n').split(':')
print(strip_func(text[0],text[1]))
    
