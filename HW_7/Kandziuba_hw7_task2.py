#Пользователь вводит с клавиатуры некоторый текст,
#после чего пользователь вводит список зарезервированных
#слов. Необходимо Находим в тексте все зарезервированные
#слова и меняем их регистр на верхний. Выводим на
#экран измененный текст. 
text = input('Enter your text: ') 
words = input('Enter reserved words: ')
words = words.split()

text = text.split() 
print(text)

symbols = ['.', ',', '!', '?', '"', ':', ';', '-', '(', ')']

for i in range(len(text)):
    if text[i][0:] in symbols:
        text[i] = text[i][1:]
    elif text[i][-1:] in symbols:
        text[i] = text[i][0:-1]

for i in range(len(text)):
    if text[i] in words:
        text[i] = text[i].capitalize()

print('That is edited text: ', " ".join(text))