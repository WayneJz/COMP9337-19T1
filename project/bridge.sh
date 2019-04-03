#!/bin/sh

name="wlan0"
bridge="evil"

brctl addbr "$bridge"
brctl addif "$bridge" wlan1
brctl addif "$bridge" "$name"mon
ifconfig wlan1 0.0.0.0 up
ifconfig "$name"mon 0.0.0.0 up
ifconfig "$bridge" up
dhclient3 "$bridge" &
