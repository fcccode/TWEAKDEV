import idaapi 


functions = Functions(0x1e10,0x2000)
for functionaddr in  functions:
    #print hex(functionaddr)
    name=GetFunctionName(functionaddr)
    #print name
    functionend = GetFunctionAttr(functionaddr, FUNCATTR_END)
    pc = 0 
    while functionaddr < functionend:
        addr = functionaddr
        if GetMnem(addr) == "mov" and GetOpnd(addr,0) =="dl":
            destaddr =GetOperandValue(addr,1)+pc
            nextaddr =  NextHead(addr)
            if  GetMnem(nextaddr) == "mov" and GetOpnd(nextaddr,0) =="dh":
                xordataAddr = GetOperandValue(nextaddr,1)+pc
                lens=0
                while addr <functionend:
                    if  GetMnem(addr) == "cmp" and GetOpnd(addr,0) =="eax":
                        lens =GetOperandValue(addr,1)
                        break
                    addr = NextHead(addr)
                data =[ chr(Byte(destaddr+i)^Byte(xordataAddr+i)) for i in range(lens)]
                print data
                data ="".join(data)
                MakeComm(destaddr , data)
        elif GetMnem(addr) == "call" and GetOpnd(addr,0)== "$+5":
             pc = NextHead(addr)
        functionaddr = NextHead(addr)
        
