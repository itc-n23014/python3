import re,pyperclip

def find_num_add(text):
    m_reg = re.compile(r'[^@^\n^\s]+@[\d\w.-]+\.[a-zA-Z]{2,}')
    p_reg = re.compile(r'(\(?\d{3}\)?[-\s]?\d{3,4}[-\s]?\d{4})')
    ml,pl = m_reg.findall(text),p_reg.findall(text)
    return ml, pl


ml, pl = find_num_add(text:=pyperclip.paste())
print(f"クリップボードから情報を取得しています.\nメアド{len(ml)}件: {', '.join(ml)} \n電話番号{len(pl)}件: {', '.join(pl)}")

