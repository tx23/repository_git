#!/bin/bash 
fpath="../cppstudy/file.c"
if [ -e $fpath ]; then 
    echo File exists;
else
    echo Does not exist;
fi
