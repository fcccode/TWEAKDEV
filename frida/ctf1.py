import frida 
import sys 

jscode = """
Java.perform(function(){

	var Incrypt = Java.use('com.h1702ctf.ctfone.InCryption');
	Incrypt.getHash.implementation = function(mystr){
		send(mystr)
		var ret = this.getHash(mystr);
        return ret
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

process = attach_to_process('com.h1702ctf.ctfone')
script=process.create_script(jscode)
script.on('message' , on_message) 
print 'start ctf' 
script.load()
sys.stdin.read()