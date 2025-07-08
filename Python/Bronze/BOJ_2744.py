word = input()

for ch in word:
    if ch.islower():
        ch = ch.upper()
    else :
        ch = ch.lower()
    print(ch,end='')

# swapcase() 활용하면 쉬움
word = input()
print(word.swapcase())