import frida 
import os 


jscode="""


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

if __name__ == "__main__":
    processname=""
