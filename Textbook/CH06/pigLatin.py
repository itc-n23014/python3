def pig_latin(text):
    return ' '.join(
        word + ('YAY' if word[0].isupper() else 'yay') if word[0] in 'aeiouAEIOU' else
        word[2:] + word[:2] + ('AY' if word[0].isupper() else 'ay') if word[:2].isalpha() and word[0] not in 'aeiouAEIOU' and word[1] not in 'aeiouAEIOU' else
        word[1:] + word[0] + ('AY' if word[0].isupper() else 'ay') if word[0].isalpha() else
        word
        for word in text.split()
    )

text = input('英文をピッグラテンに翻訳します:\n')
print(pig_latin(text))
