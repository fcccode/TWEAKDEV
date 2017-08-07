import frida 
import sys
import os 


session = frida.attach('hello')


# script = session.create_script("""
# Interceptor.attach(ptr(%s) , {
#     onEnter: function(args){
#         send(args[0].toInt32());
#     }
# });
# """% int(sys.argv[1] , 16))

# script = session.create_script("""
# Interceptor.attach(ptr(%s), { 
#     onEnter: function(args){
#         args[0] = ptr("1337") ; 
#     }
# });

# """  % int(sys.argv[1] , 16))

# script = session.create_script("""
    # recv('poke' ,function onMessage(mymessage){
        # send('pokeback')
    # }) 
# """ )

script = session.create_script("""
    var f = new NativeFunction(ptr(%s) , 'void' , ['int']) 
    f(1243534)
    f(124345)
    f(214243645)
""" % int(sys.argv[1] ,16))

def on_message(message, data):
    print message 

script.on('message', on_message)
script.load()
#script.post({"type":"poke"})
sys.stdin.read()