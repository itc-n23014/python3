import ezsheets

ID = input('スプレッドシートIDを入力:\n')

ss = ezsheets.Spreadsheet(ID)
sheet = ss[0]
for row in range(sheet.rowCount):
    data = sheet.getRow(row + 1)
    print(data)
