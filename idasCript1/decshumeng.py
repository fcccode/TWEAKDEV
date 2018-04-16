import idaapi

bytedata=0x1ac78
encDatasPtr=0x205c0
encDatasSize = 0x1da


for index in range(0,encDatasSize):
    currentStr = Dword(encDatasPtr+4*index)
    encdata = GetString(currentStr)
    #print encdata
    enclen = len(encdata)
    retstr=''
    encdatabytes=encdata.decode('hex')
    for i in range(0,enclen/2):
        keyindex=bytedata +(i%0x15) 
        decchr = Byte(keyindex) ^ ord(encdatabytes[i]) 
        #print decchr
        retstr+= str(chr(decchr))
    print retstr


    


