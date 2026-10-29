n = int(input("Enter a number"))                 # Get number from user
print(" ".rjust(3), end="")                      # Print empty space for corner
for i in range(1, n + 1):                        # Print column headings
    print(str(i).rjust(3), end="")               # Print each heading with spacing
print()                                           # Move to next line
for i in range(1, n + 1):                        # Loop through rows
    print(str(i).rjust(3), end="")               # Print row heading
    for j in range(1, n + 1):                    # Loop through columns
        print(str(i * j).rjust(3), end="")       # Print multiplication result
    print()                                       # Move to next row