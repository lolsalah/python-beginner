# School event check-in app
target_students = 4
students_checked = 0

# Formatting the name
def clean_name(name) :

    name = name.title()
    return name

# Creating the badge
def create_badge(name, grade) :

    badge_name = name[0 : 3].upper()
    badge = badge_name + str(grade)
    return badge

# Following groups
def follow_group(grade) :

    if grade <= 8 :
        return "Juniors"
    else :
        return "Seniors"

# Welcome message
def welcome(name, grade) :

    badge = create_badge(name, grade)
    group = follow_group(grade)

    print("Welcome " + name + "!")
    print("Your badge is : " + badge)
    print("Your are from " + group)

    if "a" in name.lower() :
        print("Oh wow ! Your name contians an 'A' :)")
    else :
        print("Oops ! Your name doesn't contain an 'A' :)")

    print("Enjoy your event !")
    print("-------------------------")

# Main loop
while students_checked < target_students :

    print("You are student number " + str(students_checked + 1) + " !")

    student_name = input("Enter your name : ")
    student_name = clean_name(student_name)
    student_grade = int(input("In which grade are you : "))

    welcome(student_name, student_grade)

    students_checked = students_checked + 1

# Final message
print("\n\nCheck-in completed !")
print("Total students checked-in = " + str(students_checked))
