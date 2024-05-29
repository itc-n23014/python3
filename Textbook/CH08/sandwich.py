import pyinputplus as p

price = {
    '小麦': 130, 'ホワイト': 150, 'サワー': 200,
    'チキン': 60, 'ターキー': 80, 'ハム': 20, '豆腐': 65,
    'マヨネーズ': 10, 'からし': 10, 'レタス': 15, 'トマト': 30
}

b = p.inputMenu(['小麦', 'ホワイト', 'サワー'], prompt="パンの種類を選んでください:\n")

pr = p.inputMenu(['チキン', 'ターキー', 'ハム', '豆腐'], prompt="お肉の種類を選んでください:\n")

need_chz = p.inputYesNo('チーズが必要ですか? (yes/no): ') == 'yes'
ch = p.inputMenu(['チェダー', 'スイス', 'モッツァレラ'], prompt="チーズの種類を選んでください:\n") if need_chz else False 

toppings = []
for top in ['マヨネーズ', 'からし', 'レタス', 'トマト']:
    if p.inputYesNo(f'{top}が必要ですか? (yes/no): ') == 'yes':
        toppings.append(price[top])

top_price = sum(toppings)
cheese_price = 20 if need_chz else 0
total = price[b] + price[pr] + cheese_price + top_price

num = p.inputInt(f"パンが{b}で,お肉が{pr},{ch + 'チーズ追加で' if need_chz else 'チーズ不要で'},トッピング{len(toppings)}種類でお作りすると, サンドウィッチ1つ{total}円です.\nいくつ必要ですか?: ", min=1)

print(f'サンドウィッチ{num}個で{num * total}円になります！')

