import frida 
import os 
import sys








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


def main():
    if()

if __name__ == '__main__':
    main()
packagename = "cn.tongdun.frida64"
process = attach_to_process(packagename)

script=process.create_script(jscode)
script.on('message' , on_message) 
print 'start ctf' 
script.load()
sys.stdin.read()