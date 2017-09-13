import frida 
import sys
import os 


jscode = """
    var getpid ,******; 
    var lib****** = Module.findBaseAddress('*******')
    var libc = Module.findBaseAddress('libc.so')
    console.log('libc '+libc)


    /*
    var libcexports = Module.enumerateExportsSync('libc.so')
    for(i =0 ; i < libcexports.length; i++){
        if(libcexports[i].name == "getpid"){
            console.log(libcexports[i].name)
            getpid = libcexports[i].address
        }
    }
    console.log("addr is "+ getpid)

    Interceptor.attach(getpid,{
        onEnter:function(args){
            send("6666")
        }
    });
    
    */


    var asdsadsad = Module.findExportByName('asdasdsa', "asdssadas")
    var libtde = Module.enumerateExportsSync('***********')
    for(i =0 ; i < libtde.length; i++){
        if(libtde[i].name == "***"){

            (*****) = lib*****[i].address
        }
    }
    
    Interceptor.attach(*****,{
        onEnter:function(args){
            send("7777")
        }
    });
    

"""


def on_message(message, data):
    print message 

def attach_to_process(proc_name):
    done = False
    process = None
    while not done:
        try:
            process = frida.get_usb_device().attach(proc_name)
            done = True
        except Exception:
            pass
    return process


def main():
    package="********"
    #process=attach_to_process(package)
    process =frida.get_usb_device().attach(package)
    script = process.create_script(jscode)
    script.on('message' , on_message) 
    script.load()
    sys.stdin.read()   

if __name__ == '__main__':
    main()