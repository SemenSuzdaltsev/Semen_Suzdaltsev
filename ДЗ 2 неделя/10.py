import os
x = os.path.join(os.path.dirname(__file__), "input.txt")

with open(x, 'r', encoding='utf-8') as f:
    text = f.read()
    a = 'ёЁуУеЕыЫаАоОэЭяЯиИюЮ'
    res = []
    for i, bu in enumerate(text):
        res.append(bu)
        if bu in a:
            if i > 0 and text[i-1]  not in a and not text[i-1] in a:
                res.append('с' + bu)
    print(''.join(res))