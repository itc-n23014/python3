import sys
import re

def filling(noun, adjective, verb):
    with open("sec.txt", "r") as file:
        template = file.read()

    filled = re.sub(r'\[名詞\]', noun, template)
    filled = re.sub(r'\[形容詞\]', adjective, filled)
    filled = re.sub(r'\[動詞\]', verb, filled)

    return filled

if len(sys.argv) < 4:
    print("Usage: python3 script.py [名詞] [形容詞] [動詞]")
    sys.exit(1)

noun = sys.argv[1]
adjective = sys.argv[2]
verb = sys.argv[3]

result = filling(noun, adjective, verb)
print(result)

