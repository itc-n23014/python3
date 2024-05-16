def is_valid_chess_board(table):
    if not all(len(k) == 2 and '1' <= k[0] <= '8' and 'a' <= k[1] <= 'h' for k in table): #すべてTrueじゃないとき
        return False
    types = {'pawn': 8, 'knight': 2, 'bishop': 2, 'rook': 2, 'queen': 1, 'king': 1}
    count = {'w': 0, 'b': 0} #白黒のやつ
    p_s = {'w': {ptype: 0 for ptype in types}, 'b': {ptype: 0 for ptype in types}}
    for p in table.values():
        if len(p) < 2 or p[0] not in 'wb' or p[1:] not in types:
            return False
        color, ptype = p[0], p[1:]
        count[color] += 1
        p_s[color][ptype] += 1
        if p_s[color][ptype] > types[ptype]:
            return False
    return all(count[color] <= 16 and p_s[color]['king'] == 1 for color in 'wb')



a = {'1h':'bking','6c':'wqueen','2g':'bbishop','5h':'bqueen','3e':'wking'}
b = {}
tfa = is_valid_chess_board(a)
tfb = is_valid_chess_board(b)
print(f"{a}の場合、{tfa}")
print(f"{b}の場合、{tfb}")

