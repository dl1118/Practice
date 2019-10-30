if ct == "close":
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

        print(bs)
        print(bs[1:])
        print(bs[0])
        bs = bs[1:] + bs[0]

        et += bs+ " "

        print (et)

        #write to text file
        f=open("data.txt",'a')
        f.write (ct+'\n'+et+'\n')      #clear text plus encrypted text
        f.write(et+'\n')
        f.close()

f = open("data.txt",'r')

for line in f:
    print(line)
f.close()

input("")           #pause console


        #bs = bitstring
        #a = ascii value as int
