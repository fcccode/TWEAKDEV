import frida
import os 
import sys

jscode="""
    Java.perform(function(){
       console.log("bbbbbbbbbb")
        var decode = Java.use('cn.tongdun.locationtest.MainActivity')
        decode.print.implementation  = function(str1){
            var ret = this.print(str1+"niko")
            send("23333")
            return ret
        }
    });
    


 
"""


def on_message(message ,data):
    print(message)


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
    #package="com.netease.yanxuan"
    package="cn.tongdun.locationtest"
    process=attach_to_process(package)

    script = process.create_script(jscode)
    script.on('message' , on_message) 
    print 'gogogo' 
    script.load()
    sys.stdin.read()   

if __name__ == '__main__':
    main()