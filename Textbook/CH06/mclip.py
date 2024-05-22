import sys,pyperclip

text = {'agree': 'そうですね。私も賛同します。それが良いと思います。',
        'busy': 'すみませんが、今週後半か来週にしていただけませんか？',
        'upsell': 'これを毎月の寄付にすることを検討いただけませんか？'}


if len(sys.argv) < 2:
    print('python myclip.py [キーフレーズ名]\nagree | busy | upsell の中から選択してください')
    sys.exit()
         
status = sys.argv[1]

if status in text: pyperclip.copy(text[status]); print(f"{status}に関するテキストをコピーします。")
else: print('agree | busy | upsell の中から選択してください')

