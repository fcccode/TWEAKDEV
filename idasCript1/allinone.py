import idaapi 

def strdec(location,length,xor1):
    str1=""
    for i in range(0,length):
        str1+= chr( Byte(location+i) ^ xor1)        
    print str1
    
def dumpfile(loc , length):
    pass    

def main():
    strdec(0x1c162 , 9 , 0x4f)

main()