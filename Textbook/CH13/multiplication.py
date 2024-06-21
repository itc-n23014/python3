import sys, openpyxl
from openpyxl import Workbook

def multi(n, filename='multiplication_table.xlsx'):
    wb = Workbook()
    sheet = wb.active
    sheet.title = 'Table'

    _ = [[sheet.cell(row=i + 1, column=j + 1, value=i * j) for j in range(1, n + 1)] for i in range(1, n + 1)]
    _ = [sheet.cell(row=1, column=i + 1, value=i) for i in range(1, n + 1)]
    _ = [sheet.cell(row=i + 1, column=1, value=i) for i in range(1, n + 1)]

    wb.save(filename)

if len(sys.argv) != 2:
    print("使い方: python3 script.py [数字]")
    sys.exit(1)


n = int(sys.argv[1])
multi(n)
print(f"{n}の掛け算表を'multiplication_table.xlsx'として作成しました。")

