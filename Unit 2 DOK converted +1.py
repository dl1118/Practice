ct = input("Enter a message:")
c = ""
for char in ct:
    s = ord(char)+1
    c += str(s)
ct = c
print(ct[:len(ct)])


#compared to unit 2 DOK, this only added one to ord char, nothing else.
