import os
import glob
from openpyxl import Workbook

wb, txt_files = Workbook(), glob.glob("*.txt")
ws = wb.active

[ws.append([txt_file]) for txt_file in txt_files]

wb.save("output.xlsx")

print("全てのテキストファイルがoutput.xlsxに保存されました.")

