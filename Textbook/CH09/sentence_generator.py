import sys
import re

def filling(n, a, v):
    with open("sec.txt", "r") as file:
        template = file.read()

    filled = re.sub(r'\[名詞\]', n, template)
    filled = re.sub(r'\[形容詞\]', a, filled)
    filled = re.sub(r'\[動詞\]', v, filled)

    return filled

arg = sys.argv
if len(sys.argv) < 4:
    print("Usage: python3 script.py [名詞] [形容詞] [動詞]")
    sys.exit(1)

n,a,v = arg[1],arg[2],arg[3]

result = filling(n, a, v)
print(result)
