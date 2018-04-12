function enumObject(obj) {
    for (key in obj) {
        console.log(key + ":" + obj[key])
    }
}


function newwriteCharacter(data) {
    enumObject(data)
    this.writeCharacteristic(data)
}


function hookapi() {
    var ble = Java.use("net.transpose.igniteaneandroid.IgniteANEAndroidExt");
    ble.writeSettingValue.implementation = newwriteCharacter;
}


Java.perform(hookapi)