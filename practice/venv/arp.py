
import sys
from scapy.all import *

localmac = 'e0:d5:5e:b7:86:06'
localip = '192.168.101.73'
destip = ''
ifname = 'eth0'

dst_board = 'FF:FF:FF:FF:FF:FF'
# hwdst = '00:0c:29:6c:9e:07'

result_raw = srp(Ether(src=localmac, dst='FF:FF:FF:FF:FF:FF')/ARP(op=1, hwsrc=localmac, hwdst="00:00:00:00:00:00", psrc=localip, pdst=destip), iface=ifname, verbose=False)
print(result_raw[0].res[0][1][1].fields)
# print(result_raw[0].res[0][1].getlayer(ARP).fields)
# result_raw = srp(Ether(src=localmac, dst='FF:FF:FF:FF:FF:FF')/ARP(op=1, hwsrc=localmac, hwdst='00:00:00:00:00:00', psrc=localip, pdst=destip), iface=ifname, verbose=False)
# # print(result_raw[0].res[0][1].getlayer(ARP).fields)
# result_list = result_raw[0].res
# #
# print('IP地址：' + result_list[0][1][1].getlayer(ARP).fields['psrc'] + 'MAC地址:' + result_list[0][1][1].getlayer(ARP).fields['hwsrc'])
#
#

#













