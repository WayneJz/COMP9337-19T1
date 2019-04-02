#!/bin/sh

name="wlan0"

brctl addbr evil
brctl addif evil x1
brctl addif evil at0
ifconfig x1 0.0.0.0 up
ifconfig at1 0.0.0.0 up
ifconfig evil up
dhclient3 evil &