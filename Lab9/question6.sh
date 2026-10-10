#!/bin/bash

echo "$HOME"

bc_output=$(bc << EOF
scale=5
3934/44343
EOF
)
echo "The output for 3934/44343 is" $bc_output

echo "The lines starting with D in the home are:" "$HOME"/D*

echo "The lines containing the username are:"
grep "$USER" /etc/passwd
