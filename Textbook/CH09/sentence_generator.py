import sys
import re

if len(sys.argv) < 2:
    sys.exit('使い方: sentence_generator.py src.txt')

src_file = open(sys.argv[1], 'r', encoding='utf-8') 
src_data = src_file.read()
src_file.close()


patterns = {
    '形容詞': 'かわいい',
    '名詞': 'パンダ',
    '動詞': '散歩している'
}

while True:
    mo = re.search(r'\[([^]]+)\]', src_data)
    if not mo:
        break

    pattern_name = mo.group(1)
    if pattern_name in patterns:
        repl = patterns[pattern_name]
    else:
        print(f'Please provide a replacement for {pattern_name}:')
        repl = input()

    src_data = src_data.replace(mo.group(0), repl, 1)

print(src_data, end='')

dst_file = open(sys.argv[1] + '.generated.txt', 'w', encoding='utf-8') 
dst_file.write(src_data)
dst_file.close()

