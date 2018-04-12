import frida 
import sys 

jscode = """
Java.perform(function(){

	var MainActivity = Java.use('cn.tongdun.frida64.MainActivity');
	MainActivity.stringFromJNI.implementation = function(){
		return "23333";
	}

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

def on_message(message, data):
	print message 

packagename = "cn.tongdun.frida64"
process = attach_to_process(packagename)

script=process.create_script(jscode)
script.on('message' , on_message) 
print 'start ctf' 
script.load()
sys.stdin.read()