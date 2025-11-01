land = {}
while True:
    print("--- Menu --- \n \n1. Insert Country and Capital \n2. Destroy Country and Capital \n3. Display Country \n4. Display Capital \n5. Display Country and Capital \n6. Exit")
    
    userchoitwo = input("Please choose an Option: ")
    if userchoitwo == "1":
        chosencou = input("\nInput said Country: ").capitalize()
        chosencap = input("\nInput {}'s Capital: ".format(chosencou)).capitalize()
        land[chosencou]=[chosencap]
        print("Your Country and Capital have been added.")

    elif userchoitwo == "2":
        chosencou_destroy = input("What Country and it's Capital do you wish to Destroy: ")
        del land[chosencou_destroy]
        print("You have successfully destroyed {} and it's Capital.".format(chosencou_destroy))

    elif userchoitwo == "3":
        chosencou_display = input("What Country do you wish to Display: ")
        