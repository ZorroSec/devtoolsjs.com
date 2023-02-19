#!/bin/bash

GREEN="\e[1;92m"
BLACK="\e[1;90m"

echo -e "$BLACK
/===========================\\
/  [01] Run index.py         \\
/  [02] Run index.js          \\
/==============================\\
"
read op

case $op in
    1)python3 index.py
    ;;
    2)node index.js
    ;;
esac