from umqtt.robust import MQTTClient
from machine import Pin, I2C
import utime as time
import gc
import bme280v2

client = MQTTClient("esp32-01", "iot.korivka.net")

def publish():
    while True:
        bme = bme280v2.BME280(i2c=i2c)
        temp = bme.temperature
        hum = bme.humidity
        pres = bme.pressure
        msg = "{'temp': '{}', 'hum': '{}', 'pres': '{}'  }'.format(temp, hum, pres)
        client.publish(b"v1/devices/ESP32/telemetry", msg)
        time.sleep(30)

client.reconnect()

publish()
