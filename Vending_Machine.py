# Asking costumer for his item

name = input("\n \nWhat is your name ? ")
print("\n \nHi " + name + "!, Our items are :")
print("(Nutella b-ready'1', Doritos flamin hot lemon'2', V-cola diet'3', ELmarae apple juice'4', Elano water'5')")
print("\nSorry, you can have only 1 item at once !")
Item = input("\nEnter your item's code : ")


# Informing his descesion and printing it

if Item in ["1", "2", "3", "4", "5"] :

    if Item == "1" :
        print("\nNutella b-ready : 8 $")
    elif Item == "2" :
        print("\nDoritos flamin hot lemon : 5 $")
    elif Item == "3" :
        print("\nV-cola diet : 6 $")
    elif Item == "4" :
        print("\nELmarae apple juice : 4 $")
    elif Item == "5" :
        print("\nElano water : 2 $")

else :
    print("\n \nSorry, there is no item with that code !")

# Greeting message

print("\n \nThank you for shopping with 3lewa, " + name + " !")
print("\n \nHave a great one !\n")
