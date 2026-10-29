# 9. Password Validator
# Concepts: "until" loop, for over characters, isupper()/islower()/isdigit(), a set of special
# characters, flags
# Keep asking for a password until it meets all of these rules:
# • at least 8 characters
# • at least one uppercase letter, one lowercase letter and one digit
# • at least one special character from {"!", "@", "#", "$", "%", "&", "*"}
# • no spaces
# • doesn't contain the word "password" in any case
# After each failed attempt, list every rule that was broken, not just the first one.
Special_ch={"!","@","$","^","%","&","*"}
while True:
    error=[]
    P=input("Enter Password:",)
    if len(P)<8:
        error.append("At least 8 characters password is required")
    u=False
    l=False
    digit=False
    special=False
    for i in P:
        if i.isupper():
            u=True
        if i.islower():
            l=True
        if i.isdigit():
            digit=True
        if i in Special_ch:
            special=True
    if u==False:
        error.append("Missing Uppercase Letter")
    if l==False:
        error.append("Missing Lowercase Letter")
    if digit==False:
        error.append("Missing Digit")
    if special==False:
        error.append("Missing Special Characters")
    if " " in P:
        error.append("No Space Allowed")
    if "password" in P:
        error.append("It cannot contain 'password'")
    if len(error)==0:
        print("Valid Password")
        break
    else:
        print("Invalid Password")
        for i in error:
            print(i)