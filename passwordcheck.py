master_password = str(input("Please enter your password: "))

passwordCheck = str(input("Please enter your password: "))

if (passwordCheck == master_password):
    print('You have been granted access.')
elif (master_password != passwordCheck):
    print('ACCESS DENIED, FOOL!')
