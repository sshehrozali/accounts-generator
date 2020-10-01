# Python program to generate usernames and passwords for multiple accounts # Developed by Syed Shehroz Ali #
# NOT FOR SPAMMING # # ONLY FOR GOOD PERSONAL AND COMMERCIAL USE #

# Import libraries
import hashlib
from num import test_num
from sys import exit

# Ask for how many accounts to create
print("\nHow many accounts you want to create?")

# Keep prompting till valid input
while (True):

    no = input("Enter number (only digits): ")

    check = test_num(no)

    if check == True:
        break

    print("\nInvalid Input\n")

# List for account usernames
usernames = []

# Insert names in the list
for i in range(int(no)):

    name = input("\nEnter Any name (nouns etc.): ")
    usernames.append(name)

# Open new file in "w" mode
with open("accounts.txt", "w") as file:

    # Generate five usernames and passwords
    for i in range(int(no)):

        # Get username from the list
        text = usernames[i]
        print(text)

        # Encrypt username
        encrypted = hashlib.sha224(text.encode())

        # Generate new length for username
        username_len = round(len(encrypted.hexdigest()) / 3)
        username = encrypted.hexdigest()

        # Chop off the username till new length
        new_username = username[:username_len]

        # Generate password
        password = encrypted.hexdigest()

        # Write to the file
        write = f"{i + 1}.", f"Name: {text}", " ", f"Username: {new_username}", " ", f"Password: {password}"
        file.writelines(write)
        file.write("\n")

# Success
print("\nSuccessfully generated accounts")
print("Check current directory for .txt file")
print("\nDeveloped By Syed Shehroz Ali\n")
exit(0)
