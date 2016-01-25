uppercase = str(input("Enter an uppercase letter:"))

if ord(uppercase)>=65 and ord(uppercase)<=90:
    print("Its lowercase is:",chr(ord(uppercase)+32))

else:
    print("You did not key in a uppercase letter:")
