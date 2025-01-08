def check_password(password):
    if len(password) >= 8:
        print("Strong password!")
    else:
        print("Weak password. Make it at least 8 characters long.")

password = input("Enter a password: ")
check_password(password)
