import frida 
import sys 




jscode = """
Java.perform(function(){

	var MainActivity = Java.use('com.example.seccon2015.rock_paper_scissors.MainActivity');
	MainActivity.onClick.implementation = function(v){
		send('OnClick');

		this.onClick(v);
		this.m.value = 0 ; 
		this.m.value = 1 ; 
		this.cnt.value = 999 ; 
		console.log('Done'+JSON.stringify(this.cnt));	
	}

});

"""



def on_message(message, data):
	print message 

process = frida.get_usb_device().attach('com.example.seccon2015.rock_paper_scissors')
script=process.create_script(jscode)
script.on('message' , on_message) 
print 'start ctf' 
script.load()
sys.stdin.read()