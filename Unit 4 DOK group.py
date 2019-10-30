#'''
#*Daniella Leal-Gomez
#Sara Gibbons
#Mark Messier
#COP 1000
#Unit 4 Demonstration of Knowledge
#Encrypt, read and write to a text file
#October 3, 2019
#'''

ct = input("Enter clear text:")
c = ""
for ch in ct:
    s = ord(ch)+1
    c += str(s)


decimal = ord(ch)+1

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


f = open('Unit 4.txt','a')
f.close()



