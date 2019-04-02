#!/bin/sh

name="wlan0"

ifconfig $name on
airmon-ng start $name
airodump-ng "$name"mon
