import random

print(" ____    ____  ____       ____   ____  _____ _____")
print("|    \  /    ||    \     |    \ /    |/ ___// ___/")
print("|  D  )|  o  ||  _  |    |  o  )  o  (   \_(   \_ ")
print("|    / |     ||  |  |    |   _/|     |\__  |\__  |")
print("|    \ |  _  ||  |  |    |  |  |  _  |/  \ |/  \ |")
print("|  .  \|  |  ||  |  |    |  |  |  |  |\    |\    |")
print("|__|\_||__|__||__|__|    |__|  |__|__| \___| \___|")
print("--------------------------------------------------")
print("Hello! Let's generate a password")

### Define a list of characters
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()"

### Promt the user
passwordLength = int(input("How long would you like your password to be? "))

### Generate a random password
newPassword = []
for x in range(passwordLength):
    ###Append a random character to the password string
    newPassword.append(random.choice(characters))

### join whole ost back to a string
finalPassword = ''.join(map(str, newPassword))

###new password
print("\n This is your new password: ",finalPassword)