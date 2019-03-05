#Set password
PASSWORD = "Hello Kitty"

PASSWORD_PROMPT = "Password: "

userAttempt = input(PASSWORD_PROMPT)

while userAttempt != PASSWORD:
    print("That is incorrect. >:(")

    userAttempt = input(PASSWORD_PROMPT)


print("That is correct!")
