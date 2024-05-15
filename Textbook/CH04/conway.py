import random, time, copy

W, H = 60, 20
n_cell = [['#' if random.randint(0, 1) == 0 else ' ' for _ in range(H)] for _ in range(W)] #最初のセルの作成

while True:
    print('\n' * 4 + '\n'.join(''.join(n_cell[x][y] for x in range(W)) for y in range(H))) #作ったセルを表示する
    c_cell = copy.deepcopy(n_cell)
    
    for x in range(W): #座標から隣接したセルをしらべる
        for y in range(H):
            neighbor = sum(
                c_cell[(x+dx) % W][(y+dy) % H] == '#'
                for dx in (-1, 0, 1) for dy in (-1, 0, 1)
                if dx != 0 or dy != 0
            )
            n_cell[x][y] = '#' if neighbor == 3 or (neighbor == 2 and c_cell[x][y] == '#') else ' '
    
    time.sleep(1)

