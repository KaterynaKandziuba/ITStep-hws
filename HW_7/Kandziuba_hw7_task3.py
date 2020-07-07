# Есть некоторый текст. Посчитаnm в этом тексте количество предложений 
# и вывести на экран результат.

text = input('Enter your text: ') 

match = 0 #counter for loop
a = 0 #position of entered dot
b = 0 #position of entered exclamation mark
c = 0 #position of entered question mark
count = 0 #counter of marks
for i in text:
	match = match + 1
	a = text.find('.', a)
	if match == a:
		count += 1
		a += 1
	b = text.find('!', b)
	if match == b:
		count += 1
		b += 1
	c = text.find('?', c)
	if match == c:
		count += 1
		c += 1
print ("There are", count, "sentenses.")