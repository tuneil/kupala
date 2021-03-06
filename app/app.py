from umqtt.robust import MQTTClient
from machine import Pin, I2C

import gc
import json
import utime as time
import app.bme280v2 as bme280

import network
import ubinascii

client = MQTTClient("esp32-01", "iot.korivka.net")
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)

def publish():
    try:
            bme = bme280.BME280(i2c=i2c)
            temp = bme.temperature
            hum = bme.humidity
            pres = bme.pressure
            cli = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    except:
            temp = "NA"
            hum = "NA"
            pres = "NA"
    msg = json.dumps(dict(temp=temp, hum=hum, pres=pres, cli=cli))
    print(msg)
    client.publish(b"v1/devices/ESP32/telemetry", msg)
    time.sleep(30)

while True:
   client.reconnect()
   publish()
