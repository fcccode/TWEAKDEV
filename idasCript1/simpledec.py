import idaapi 
str1=""
for i in range(0,29):
    str1+= str(chr(Byte(0xc05B+i) ^0x3d))
print str1
str1=""
for i in range(0,7):
    str1+= str(chr(Byte(0xc079+i) ^0x2c))
print str1

str1=""
for i in range(0,3):
    str1+= str(chr(Byte(0xc081+i) ^0x58))
print str1