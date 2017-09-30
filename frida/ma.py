import frida 
import os 
import sys

jscode="""
    var funcOff = 0x1e19c8  
    var mono_open =undefined
    while(mono_open ==undefined){
        var mono_open = Module.findExportByName('libmono.so','mono_image_open_from_data_with_name') 
    }
    //send(mono_open)
    var addr = Module.findBaseAddress('libmono.so')
    var addrnum = new Number(addr)
    //send(addr)
    //send(funcOff+addrnum)
    var func = new NativePointer(ptr(addrnum+funcOff))
    Interceptor.attach(func, {
        onEnter: function(args){
            var dlladdr = args[0]
            var size = args[1].toInt32()
            var data=Memory.readByteArray(dlladdr, size)
            //send(dlladdr)
            console.log("size "+size)
            send("data",data)
        }
    })
"""

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

def on_message(message,data):
    print message
    data2 = message['payload']
    if data2=="data":
        print len(data)
        with open(str(len(data))+".dll" , 'wb') as fd :
            fd.write(data)

process = attach_to_process('com.netease.ma.netease')
script=process.create_script(jscode)
script.on('message' , on_message) 
print 'start'
script.load()
sys.stdin.read()