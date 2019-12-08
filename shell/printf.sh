#!/bin/bash

printf "%-5s %-10s %-4s\n" No Name Mark
echo -e "\033[1;34m Green text \033[0m"
echo -e "\033[1;44m Green Background \033[0m"
if [ $? -eq 0 ];
then
    echo "$CMD executed successfully"
else
    echo "$CMD terminated unsuccessfully"
    fi
