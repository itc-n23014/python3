name = input("あなたの名前を入力してください: ")
print(f"こんにちは,{name}さん\n名前は{len(name)}文字です.")
age = int(input("続いて,年齢を入力してください: "))
print("未成年です." if age < 20 else "成人しています.")

