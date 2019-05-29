# COMP9337-19T1

COMP9337 Securing Wireless Networks 2019T1

Lecturer in charge: Sanjay Jha

Mark: 89 HD, awarded 3rd place in this course

## Labs

1. Introduction to basic cryptographic mechanisms

2. Hacking Wireless Networks

3. MITM Attack and Evil Twin AP

4. Wireshark analysis of HTTPS (in-lab hand-in)

5. SNORT IDS

## Project

### Project Summary

This project is a set of penetration test on wireless network, the steps of the implementation are:

1. Build a fake AP, DHCP server and web server, then allow victims to connect.

2. Disconnect victims from original AP by deauth attack.

3. When connect, direct victims to the fake AP portal (runs on web sever), and let victims type real confidentials of the original AP.

4. When get the confidentials, stop the fake AP. Now, victims and attacker both connect to the original AP, then use the confidentials to crack into the backend of original AP.

5. Change the original DNS server IP address to the attacker's IP address.

6. Build a DNS server on attacker's machine. Then use DNS poisoning to direct a website (with login pages) to the attacker's web server, remaining other DNS requests as normal.

7. As all DNS requests sent to the attacker, when victims query the paticular website, they will be directed to the attacker's web server and let victims type real confidentials.

8. Get user confidentials of a particular website.

9. In the local network, find a vulnerable website which allows remote shell execution (This can be easy implemented by PHP). For simple implementation, the privilege of PHP script execution and web server user can be set as "root".

10. Create a reverse shell on victim machine, create, edit and delete a txt file on victim machine without any awareness.

### Project Notes

1. `dnsmasq` is a useful tool that can configure DNS and DHCP. Note that `dnsmasq` and `dhcpd` may **NOT** work simultaneously.

2. Click [Here](https://www.hi-linux.com/posts/17088.html) for more `dnsmasq` references.

3. The steps to create the attacker environment are following:

    - You should install Kali Linux. `dnsmasq`, `dhcpd`, `nginx` webserver and `php server` are also required.

    - Execute `./twinstart.sh` , if you see `at0` then go ahead. If not, please kill all other `airbase-ng` processes. You may need to modify this shell script for your own.

    - Execute `./settings.sh` to configure `dnsmasq` and `iptables`, to allocate IP addresses for victim client and forward any packets from victim users. You may need to modify this shell script for your own.

    - Execute `python3 backend.py` to enable attacker backend.

    - Execute `./deauth.sh` to enable deauthentication attack. You may need to modify this shell script for your own. Optionally, execute `./monitor.sh` to
    monitor the WLAN flows.

    - For reverse shell implementation, copy `reverse.php` and `rshell.html` to your **victim** web directory. You may also grant privileges for reverse shell execution.
