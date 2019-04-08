# COMP9337-19T1
COMP9337 Securing Wireless Networks 2019T1

#### Project Notes
1. `dnsmasq` is a tool that can configure DNS and DHCP. Note that `dnsmasq` and `dhcpd` may **NOT** work simultaneously.

2. Click [Here](https://www.hi-linux.com/posts/17088.html) for `dnsmasq` references.

3. The steps to create a fake AP (Evil Twin) are following:
    
    - Execute `./twinstart.sh` , if you see `at0` then go ahead. If not, please kill all other `airbase-ng` processes.
    
    - Execute `./settings.sh` to configure `dnsmasq` and `iptables`, to allocate IP addresses for victim client and 
    forward any packets from victim users.
