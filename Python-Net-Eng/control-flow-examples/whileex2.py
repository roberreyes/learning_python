username = input("Please enter your username: ")
while len(username) < 8:
    print("FAILED! username must be at least 8 characters")
    username = input("Please enter your username: ")
