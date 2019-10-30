message = input("Enter a one-word, lowercase message:")
distance = int(input("Enter the distance value:"))

code = ""
for ch in message:
    ordValue = ord(ch)
    cipherValue = distance + ordValue
    if cipherValue > ord('~'):
        cipherValue = ord('!') + distance - \
                      (ord('~') - ordValue + 1)
    code += chr(cipherValue)
print(code)
