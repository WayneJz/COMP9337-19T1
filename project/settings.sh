#!/bin/sh

name="wlan0"

mv dhcpd.conf /etc/dhcp/dhcpd.conf

ifconfig at0 up
ifconfig at0 10.0.0.1 netmask 255.255.255.0
echo 1 > /proc/sys/net/ipv4/ip_forward
route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1

iptables --flush
iptables --table nat --flush
iptables --delete-chain
iptables --table nat --delete-chain
iptables -P FORWARD ACCEPT
iptables --append FORWARD --in-interface at0 -j ACCEPT
iptables --table nat --append POSTROUTING --out-interface "$name" -j MASQUERADE
iptables -A FORWARD -p tcp --syn -s 10.0.0.0/24 -j TCPMSS  --clamp-mss-to-pmtu
iptables -t nat -A PREROUTING -p tcp -m multiport --dport 80,8080 -j DNAT --to 10.0.0.1:80

dhcpd -cf /etc/dhcp/dhcpd.conf at0
