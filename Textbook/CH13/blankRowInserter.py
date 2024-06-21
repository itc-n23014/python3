import sys
from openpyxl import load_workbook

if len(sys.argv) != 3:
    print("使い方:python3 script.py [N] [M]\nN行目にM行の空白を挿入.")
    sys.exit(1)

filename = "myProduce.xlsx"
start_row, num_rows = int(sys.argv[1]), int(sys.argv[2])


wb = load_workbook(filename)
ws = wb.active
ws.insert_rows(start_row, amount=num_rows)

wb.save(filename)
print(f"空行を{num_rows}行挿入して上書き保存しました。")

