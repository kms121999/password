#Set password
PASSWORD = "Hello Kitty"

PASSWORD_PROMPT = "Password: "

userAttempt = input(PASSWORD_PROMPT)

failedAttempts = 0
while userAttempt != PASSWORD:
    failedAttempts += 1
    print("That is incorrect. >:(")
    print("You have guessed incorectly", failedAttempts, "times.")

    userAttempt = input(PASSWORD_PROMPT)


print("That is correct!")
