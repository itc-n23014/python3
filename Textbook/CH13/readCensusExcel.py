import openpyxl, pprint  
print('ワークブックを開いています...')
wb = openpyxl.load_workbook('censuspopdata.xlsx') #ファイル指定
sheet = wb['Population by Census Tract']   #どのシートか
county_data = {}

print('行を読み込んでいます...')
for row in range(2, sheet.max_row + 1): 
    state = sheet[f'B{str(row)}'].value
    county = sheet[f'C{str(row)}'].value
    pop = sheet[f'D{str(row)}'].value

    county_data.setdefault(state, {}) 
    county_data[state].setdefault(county, {'地域数': 0, '人口': 0}) 

    county_data[state][county]['地域数'] += 1
    county_data[state][county]['人口'] += int(pop)  

print('結果を書き込み中...')
result_file = open('census2010.py', 'w')
result_file.write(f'all_data = {pprint.pformat(county_data)}')
result_file.close()
print('完了')
