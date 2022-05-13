#!/bin/bash
cd <Path of the alert folder>
while :
do
        d=$(date +%H)
        if [ $d = 00 ]
        then
                  sudo find . -mtime +<Without space mention the no of days older data you wanna remove> -delete;
        fi
        sleep 2h
done
