import pyperclip

text = pyperclip.paste()
pyperclip.copy('\n'.join([f"* {i}" for i in text.split('\n')]))
