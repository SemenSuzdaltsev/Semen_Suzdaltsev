import string

import os
x = os.path.join(os.path.dirname(__file__), "text_pyth.txt")
with open(x, 'r', encoding='utf-8') as f:
    text = f.read()

for punct in string.punctuation:
    text = text.replace(punct, ' ')

text = text.lower()
words = text.split()  
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

items = list(word_count.items())
items.sort(key=lambda x: x[1], reverse=True)
print(f"{'Слово':<20}{'Количество':>10}")
for word, count in items[:10]:
    print(f"{word:<20}{count:>10}")

