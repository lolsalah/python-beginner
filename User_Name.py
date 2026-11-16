# Asking user for his name
user_name = input("Enter your name : ")

# Formatting the name
user_name_formatted = user_name.lower().replace(" ", "_")

# Checking if the name is accepted
if len(user_name_formatted) < 5 :
    print("User name is short.")
elif "admin" in user_name_formatted :
    print("User name can't contain 'admin'")
else :
    print("User name accepted : ", user_name_formatted)
