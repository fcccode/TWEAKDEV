# copy from web
from unicorn import * 
from unicorn.x86_const import *
from pwn import * 

PENTRY = 0x400670
FEND =  [0x4006f1,0x400709]

BASE = 0x400000
STACK_ADDR = 0x0  
STACK_SIZE = 1024 * 1024 

insskip=[0x4004ef , 0x4004f6 ,0x400502,0x40054f]
stack = []
d={}

def hook_code(mu,address ,size , user_data):
    #print('>>> Tracing instruction at 0x%x, instruction size = 0x%x' %(address, size))
    if address in insskip :
        mu.reg_write(UC_X86_REG_RIP,address+size)
    elif address == 0x400560:
        c = mu.reg_read(UC_X86_REG_RDI)
        print(chr(c))
        mu.reg_write(UC_X86_REG_RIP,address+size)
    elif address == PENTRY:                # Are we at the beginning of fibonacci function?
        arg0 = mu.reg_read(UC_X86_REG_RDI)          # Read the first argument. Tt is passed via RDI
        r_rsi = mu.reg_read(UC_X86_REG_RSI)         # Read the second argument which is a reference
        arg1 = u32(mu.mem_read(r_rsi, 4))           # Read the second argument from reference
        
        if (arg0,arg1) in d:                        # Check whether return values for this function are already saved.
            (ret_rax, ret_ref) = d[(arg0,arg1)]
            mu.reg_write(UC_X86_REG_RAX, ret_rax)   # Set return value in RAX register
            mu.mem_write(r_rsi, p32(ret_ref))       # Set retun value through reference
            mu.reg_write(UC_X86_REG_RIP, 0x400582)  # Set RIP to point at RET instruction. We want to return from fibonacci function
            
        else:
            stack.append((arg0,arg1,r_rsi))         # If return values are not saved for these arguments, add them to stack.
        
    elif address in FEND:
        (arg0, arg1, r_rsi) = stack.pop()           # We know arguments when exiting the function
        
        ret_rax = mu.reg_read(UC_X86_REG_RAX)       # Read the return value that is stored in RAX
        ret_ref = u32(mu.mem_read(r_rsi,4))         # Read the return value that is passed reference
        d[(arg0, arg1)]=(ret_rax, ret_ref)  

def readfile(file):
    with open(file) as fd :
        return fd.read() 

def main():
    mu = Uc(UC_ARCH_X86,UC_MODE_64)
    mu.mem_map(BASE , 1024*1024)
    mu.mem_map(STACK_ADDR,STACK_SIZE)
    mu.mem_write(BASE, read('./fibonacci'))
    mu.reg_write(UC_X86_REG_RSP , STACK_ADDR+STACK_SIZE-1)
    mu.hook_add(UC_HOOK_CODE,hook_code)
    mu.emu_start(0x4004e0,0x400575)

if __name__ == '__main__':
    main()
