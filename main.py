from umqtt.robust import MQTTClient
import machine
import utime as time
import gc
#import bme280

client = MQTTClient("esp32-01", "iot.korivka.net")
pin5 = machine.Pin(5, machine.Pin.OUT)

i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))
#bme = bme280.BME280(i2c=i2c)

def publish():
    count = 1
    while True:
        pin5.value(0)
#        v = bme.values
#        msg = b'{"MsgId":%u,"Mem":%u,"Celsius":%s,"Pressure":%s,"Humidity":%s}' % (count, gc.mem_free(), v[0][:-1], v[1][:-3], v[2][:-1])
        client.publish(b"v1/devices/ESP32/telemetry", msg)
        pin5.value(1)
        count = count + 1
        time.sleep(30)

client.reconnect()

publish()
