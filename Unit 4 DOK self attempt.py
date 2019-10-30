

ct = input("Enter clear text:")
c = ""
for ch in ct:
    s = ord(ch)+1
    c += str(s)
print(c, end = " ")

if ct == "close":
    break
else: et = ""

decimal = ord(ch)+1
print(decimal)

if decimal == 0:
    print(0)
else:
    bitString = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        bitString = str(remainder) + bitString
    print(bitString)

    s1 = bitString[1:]
    s0 = bitString[0]  

    et = s1+s0

    print(et)


    f=open("4DOK.txt",'a')
    f.write(ct+'\n'+et+'\n')
    f.close()

f=open("4DOK.txt",'r')

for line in f:
    print(line)
f.close

input("")
