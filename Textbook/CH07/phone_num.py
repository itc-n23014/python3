def phone_num(text):
	return len(text) == 12 and all([i.isdecimal() for i in text.split('-')]) and [text[3],text[7]] == ['-','-']
    


p = input("電話番号を入力してください: ")
print(phone_num(p))
