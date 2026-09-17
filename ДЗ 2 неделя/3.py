alph = {
    'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O',
    'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
    'Y': 'Y', '1': '1', '8': '8',
    'E': '3',
    'J': 'L',
    'S': '2',
    'Z': '5',
    '3': 'E',
    'L': 'J',
    '2': 'S',
    '5': 'Z'
}
s = input().strip()
mirT = True
mir = []

for i in s:
    if i in alph:
        mir.append(alph[i])
    else:
        mirT = False
        break
        
if mirT:
    mirs = "".join(mir)[::-1]
    if mirs != s:
        mirT = False

if s == s[::-1] and mirT:
    print(f"{s} is a mirrored palindrome.")
elif s == s[::-1]:
    print(f"{s} is a regular palindrome.")
elif mirT:
    print(f"{s} is a mirrored string.")
else:
    print(f"{s} is not a palindrome.")
