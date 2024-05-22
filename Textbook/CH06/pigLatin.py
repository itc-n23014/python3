def pig_latin(text):
    words = text.split()
    pig_latin_words = []

    for word in words:
        if word[0].isalpha():
            if word[0] in 'aeiouAEIOU':
                pig_word = word + 'yay'
            elif word[0] not in 'aeiouAEIOU' and word[1] not in 'aeiouAEIOU' and word[:2].isalpha():
                pig_word = word[2:] + word[:2] + 'ay'
            else:
                pig_word = word[1:] + word[0] + 'ay'
        else:
            pig_word = word
        
        pig_latin_words.append(pig_word)
    
    return ' '.join(pig_latin_words)

text = input()
print(pig_latin(text))

