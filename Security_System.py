# Simple Smart Home Security System
system_active = True
in_night_mode = False
is_student = True
has_id = True
security_code = int(input("\n\n\n\n\nEnter the security code : "))
temperature = int(input("\n\nWhat is the temperature ? "))

# Allowing access
if system_active and not in_night_mode :
    if is_student :
        if has_id :
            print("\n\nAccess is allowed ! Welcome student !")
        else :
            print("\n\nStudent is missing the ID !")
    else :
        print("\n\nOnly students are granted to access !")
else :
    print("\n\nAccess is denied ! System is not activated or in night mode !")

# Security code checking
if security_code % 2 == 0 :
    print("\n\nSecurity code is even.")
else :
    print("\n\nSecurity code is odd.")

# Temperature checking
if temperature > 30 :
    print("\n\nIt's too hot, AC is turned on !")
elif temperature < 20 :
    print("\n\nIt's too cold, heater is turned on !")
else :
    print("\n\nNormal temperature !")
