#!/bin/bash

file=SOCR-HeightWeight_data.csv
while IFS=',' read -r col1 col2 col3; do
	echo "Column1: $col1 | Column2: $col2  | Column3: $col3"
done < "$file"
