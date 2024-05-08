import random, sys

print('最初はグー,じゃんけん…')

win, losse, tie = 0, 0, 0
moves = {'r': 'グー', 'p': 'パー', 's': 'チョキ'}

while True:
    
    move = input('(r)グー (p)パー (s)チョキ or (q)やめる: ')
    if move == 'q': sys.exit()
    if move not in moves: print('r,p,s,qの中から選択してください.'); continue

    move2 = random.choice(list(moves.keys()))
    print(f'{moves[move]} 対 {moves[move2]}')

    if move == move2:
        print('あいこ!')
        tie += 1
    elif (move == 'r' and move2 == 's') or \
         (move == 'p' and move2 == 'r') or \
         (move == 's' and move2 == 'p'):
        print('勝ち!')
        win += 1
    else:
        print('負け!')
        losse += 1

    print(f'{win} 勝ち, {losse} 負け, {tie} あいこ')

