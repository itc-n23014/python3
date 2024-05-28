def phone_num(text):
	return len(text) == 12 and all([i.isdecimal() for i in '415-555-4242'.split('-')]) and [text[3],text[7]] == ['-','-']
    

    







p = input() #415-555-4242
print(phone_num(p))
