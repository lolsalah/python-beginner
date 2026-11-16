# Set correct password
correct_password = "Ali"

# Set attempts
max_attempts = 3
attempts = 0

# Input and checking
while attempts < max_attempts :

    password = input("Enter your password : ")

    if password == correct_password :
        print("Correct password !")
        break
    else :
        print("Incorrect password !")

    if password[0] == correct_password[0] :
        print("Wrong password ,but first letter is correct !")

    attempts = attempts + 1

    print("remainig attempts : ",max_attempts - attempts)

if attempts == max_attempts :
    print("You've reached your maximum attempts limit !")
