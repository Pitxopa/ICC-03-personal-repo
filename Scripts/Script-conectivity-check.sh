#!/bin/bash
echo "Input the IPAddress to check:"
read input 

# Conectivity Check
if ping -c 1 $input &> /dev/null; then
       echo "Host is reacheable"
else
       echo "Host NOT reacheable"
fi