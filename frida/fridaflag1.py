import frida 
import os 
import sys

jscode="""
Java.perform(function() {

    var Act = Java.use('org.team_sik.flagvalidator.MainActivity');

    Act.value.implementation = function(){
        var ret = nativeValue.call(this);
        send("Part 3 => " + ret);
        return ret;
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

if __name__ == "__main__":
    processname="org.team_sik.flagvalidator"
    process = attach_to_process(processname)
    script=process.create_script(jscode)
    script.on('message' , on_message) 
    print 'start ctf' 
    script.load()
    sys.stdin.read()
