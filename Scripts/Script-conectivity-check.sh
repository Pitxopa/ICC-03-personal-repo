#!/bin/bash

# Displays logo and version to the user 
cat << "EOF"
  _   _      _    _____ _               _    
 | \ | |    | |  / ____| |             | |   
 |  \| | ___| |_| |    | |__   ___  ___| | __
 | . ` |/ _ \ __| |    | '_ \ / _ \/ __| |/ /
 | |\  |  __/ |_| |____| | | |  __/ (__|   < 
 |_|_\_|\___|\__|\_____|_| |_|\___|\___|_|\_\
 |__   __| |          | |            | |     
    | |  | |__   ___  | |_ ___   ___ | |     
    | |  | '_ \ / _ \ | __/ _ \ / _ \| |     
    | |  | | | |  __/ | || (_) | (_) | |     
    |_|  |_| |_|\___|  \__\___/ \___/|_|     
                                             
EOF

echo "Version 1.0.0"
echo "by The Super HackerMan"

# Asks for the user input
#echo -e "\nInput the IPAddress to check:"
#read input 

#echo "<------------checking:------------>"

# Conditional statement

# IF Statement:
# Pings the user input
#if ping -c 1 $input &> /dev/null; then
#        echo -e "\nHost is reacheable"
#else
#        echo "Host NOT reacheable"
#fi

echo -e "\nChoose an option:"
echo "1) Ping the target"
echo "2) Route to target"
read option

echo -e "\nInput the IPAddress to check:"
read input

# Case Statement
case $option in 
         1) ping -c 1 $input ;;
         2) traceroute $input ;; 
         *) echo "Invalid option, please choose 1) for ping or 2) for traceroute!" ;; 
esac 