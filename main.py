import network
import upip
from app.otaUpdate import OTAUpdater

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
    o = OTAUpdater('https://github.com/tuneil/kupala')
    o.check_for_update_to_install_during_next_reboot()
    o.download_and_install_update_if_available('McDonalds', 'eternity8')

def install_packages():
    try:
        import umqtt.robust
    except:
        upip.install('micropython-umqtt.robust')

if __name__ == "__main__":
    do_connect()
    download_and_install_update_if_available()
    install_packages()
