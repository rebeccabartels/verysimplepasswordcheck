def validate_password(password):
    # Inside the function, check if the password is longer than 6 characters long
    if (len(password) > 6):
        return True
    else:
        return False


passwordToCheck = input("Enter the password to check: ")
result = validate_password(passwordToCheck)


print(result)
