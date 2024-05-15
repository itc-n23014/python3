def comma(a):
    return  ', '.join(a[:-1]) + ', and ' + a[-1] + '.'

a = input("単語をスペース区切りで入力してください:").split()
print(comma(a))

