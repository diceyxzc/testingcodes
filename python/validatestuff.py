print("---------------------------------------")
print("Username is no more than 12 characters.")
print("Does not contain any spaces.")
print("Does not contain any digits.")
print("---------------------------------------")
username = str(input("Enter a username: "))

if len(username) > 12:
    print("Invalid username (Contains more than 12 characters).")
elif not username.find(" ") == -1:
    print("Invalid username (Contains space).")
elif not username.isalpha ():
    print("Invalid username (Contains digit).")
else:
    print("Valid username.")