const trace = require('frida-trace')

const func = trace.func
const argIn = trace.argIn
const argOut = trace.argOut
const retVal = trace.retval

const types = trace.types
const pointer = types.pointer
const INT = types.INT
const UTF8 = types.UTF8
const POINTER = types.POINTER




trace({
    module: 'libc.so',
    functions: [
        func('getpid', retVal(INT))
    ],
    callbacks: {
        onEvent(event) {
            console.log("23333")
        }
    }
})