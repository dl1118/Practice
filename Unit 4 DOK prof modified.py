ct = input("Enter clear text:")
c = ""
for char in ct:
    s = ord(char)+1
    c = str(s)
    #print(c, end = " ")

if s == 0:
    print(0)
else:
    bitString = ""
    while s > 0:
        remainder = s % 2
        s = s // 2
        bitString = str(remainder) + bitString
        print(bitString, end = " ")

#s1 = bitString[1:]
#s0 = bitString[0]

#et = s1+s0

#print(et)


if ct== "Close":
    break
else: et = ""
a = 0


for c in ct:
    bs = ""
    a += ord(c) + 1

    while a >0:         #convert ascii to binary
        r  = a%2
        a //=2
        bs = str(r) + bs

        #print(bs)
        #print(bs[1:])
        #print(bs[0])
        bs = bs[1:] + bs[0]

        et += bs+ " "

        #print (et)

        #write to text file
        f=open("data.txt",'a')
        #f.write (ct+'\n'+et+'\n')      #clear text plus encrypted text
        f.write(et+'\n')
        f.close()

f = open("data.txt",'r')

for line in f:
    print(line)
f.close()

input("")           #pause console


        #bs = bitstring
        #a = ascii value as int
