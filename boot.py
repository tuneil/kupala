import network
import otaUpdate
import upip
from ota_update.main.ota_updater import OTAUpdater

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect("McDonalds", "eternity8")
        while not wlan.isconnected():
            pass
    print("network config:", wlan.ifconfig())

def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/tuneil/kupala.git')
    o.download_and_install_update_if_available('McDonalds', 'eternity8')

def install_packages():
    upip.install('micropython-umqtt.simple')
    upip.install('micropython-umqtt.robust')

if __name__ == "__main__":
    do_connect()
    download_and_install_update_if_available()
    install_packages()
