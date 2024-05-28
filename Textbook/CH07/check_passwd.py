import re

def check_password(passwd):
    s = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$')
    return '良いパスワードです' if s.match(passwd) else '8文字以上[大小文字、数字を含む]に設定してください。'


p = input("パスワードを作成してください:")
print(check_password(p))
