# Reading challenge tracker
pages = 24
days = 1

# Greeting message
print("Start your reading challenge !\n\n")

# Days counter
while pages > 6 :

    print("It's day " + str(days) + ", " + str(pages) + " pages left !")

    energy = input("Tell me your energy is high or low : ")

    if energy.lower() == "high" :
        print("Great ! Read 6 pages !")
        pages = pages - 6
    elif energy.lower() == "low" :
        print("No worries ! Read only 3 pages !")
        pages = pages - 3

    days = days + 1
    
    print("-------------------------")

#Final message
print("You've reached your goal in " + str(days - 1) + " days, " + str(pages) +" pages are finally left !")
