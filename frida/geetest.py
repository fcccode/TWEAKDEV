import os 
import frida 
import sys

jscode2="""
Java.perform(function(){
   var Request = Java.use('com.geetest.onepass.O0000o0') ;//  https class
   var rsaenc = Java.use('com.geetest.onepass.O0000o0') ;
   


});
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

process = attach_to_process('com.example.geeonepassdemo')
script=process.create_script(jscode2)
script.on('message' , on_message) 
print 'start ctf' 
script.load()
sys.stdin.read()