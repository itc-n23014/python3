import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb['Sheet']

n_price = {'Garlic': 3.07, 'Celery': 1.19, 'Lemon': 1.27}

#リスト内でへんしゅうする
_ = [sheet.cell(row=r, column=2, value=n_price[name]) for r in range(2, sheet.max_row + 1) if (name := sheet.cell(row=r, column=1).value) in n_price]

wb.save('updatedProduceSales.xlsx')

