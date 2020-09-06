from scapy.all import *
import socket
import fcntl
import struct
import optparse


def get_arp(ip_address, ifname):
    localip = get_ip_address(ifname)


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(s, '-----test---->')
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', (ifname[:15]).encode())
    )[20:24])


if __name__ == "__main__":
    parser = optparse.OptionParser('用法：\n python3 GET_IP.py --ifname 接口名')
    parser.add_option('--ifname', dest='ifname', type='string', help='要查询的接口的名字')
    (options, args) = parser.parse_args()
    ifname = options.ifname
    if ifname == None:
        print(parser.usage)
    else:
        print(get_ip_address(ifname))

# dsasdasd asdad a
