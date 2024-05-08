import random, sys

print('最初はグー,じゃんけん…')

wins, losses, ties = 0, 0, 0
moves = {'r': 'グー', 'p': 'パー', 's': 'チョキ'}

while True:
    
    player_move = input('(r)グー (p)パー (s)チョキ or (q)やめる: ')
    if player_move == 'q': sys.exit()
    if player_move not in moves: print('r,p,s,qの中から選択してください.'); continue

    computer_move = random.choice(list(moves.keys()))
    print(f'{moves[player_move]} 対 {moves[computer_move]}')

    if player_move == computer_move:
        print('あいこ!')
        ties += 1
    elif (player_move == 'r' and computer_move == 's') or \
         (player_move == 'p' and computer_move == 'r') or \
         (player_move == 's' and computer_move == 'p'):
        print('勝ち!')
        wins += 1
    else:
        print('負け!')
        losses += 1

    print(f'{wins} 勝ち, {losses} 負け, {ties} あいこ')

