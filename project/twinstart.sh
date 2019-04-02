#!/bin/sh

name="wlan0"

ifconfig $name up
airmon-ng start $name
nohup airbase-ng -e "Starbucks" -c 4 "$name"mon &
