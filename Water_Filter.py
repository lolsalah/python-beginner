# Clean water station monitor
containers = 6
clean_target = 3
cleaned = 0

# Containers checking
print("Checking containers...")

    # main loop
for container in range(1, containers + 1) :

    print("\n\nChecking container number " ,container)

    if container == 2 or container == 5 :
        print("Container is contiminated !")
        continue
    else :
        print("Container is clean !")
        cleaned = cleaned + 1

    if cleaned == clean_target :
        print("\n\nReached clean containers target : "+ str(cleaned) +" !")
        break
