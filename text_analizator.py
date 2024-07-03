text = input("введите текст для анализа: ")
text = text.lower()
punctuation = ['.', ',','?','!']
for char in punctuation:
    text = text.replace(char,'')

words = text.split()
print(words)


print(len(set(words)))

word_frequency = {}
for i in words:
    if i in word_frequency:
        word_frequency[i] +=1
    else:
        word_frequency[i] =1
print(word_frequency)
min = len(words[0])

for i in words:
    if len(i) < min:
        min = len(i)

for i in words:
    if len(i) == min:
        print(i)
max = 0
for i in words:
    if len(i) > max:
        max = len(i)
for i in list(set(words)):
    if len(i) == max:
        print(i)