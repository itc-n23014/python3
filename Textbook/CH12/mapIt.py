# 引数、またはクリップボードの場所をMapで表示するコード
import webbrowser,sys,pyperclip
arg = sys.argv

if len(arg) < 2:
    print('クリップボード上の場所を検索しています...')
    p = pyperclip.paste().split()
    webbrowser.open(f'https://www.google.com/maps/place/{"+".join(p)}')
else:
    print('GoogleMapから引数の場所を検索します...')
    webbrowser.open(f'https://www.google.com/maps/place/{"+".join(arg[1:])}')




