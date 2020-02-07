from umqtt.robust import MQTTClient
import machine
import utime as time
import gc

client = MQTTClient("esp32-01", "iot.korivka.net")
pin5 = machine.Pin(5, machine.Pin.OUT)

i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))

def publish():
    count = 1
    while True:
        pin5.value(0)
        client.publish(b"v1/devices/ESP32/telemetry", msg)
        pin5.value(1)
        count = count + 1
        time.sleep(30)

client.reconnect()

publish()
