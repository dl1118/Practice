coded = input("Enter the coded text:")
value = int(input("Enter the distance value:"))

dc = ""

for ch in coded:
    ordvalue = ord(ch)
    cipherValue = ordvalue - value
    if cipherValue < ord('a'):
        cipherValue = ord('z')

    dc += chr(cipherValue)
print(dc)
