import webbrowser,sys
arg = sys.argv

if len(arg) < 2:
    raise Exception("引数を指定してください.[python3 web.py 場所]")

webbrowser.open(f'https://www.google.com/maps/place/{"+".join(arg[1:])}')




