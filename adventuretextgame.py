name = str(input("Enter Your Name: "))
print(f"{name} you are trapped in a dungeon with your friend. You see a barrel.")
print("What do you do?")
print("1.Move the barrel 2.Climb the barrel")
user = int(input("Choose 1 or 2: "))
if user == 1:
    print("The barrel moves aside and you find a secret tunnel.")
    print("What do you do?")
    print("1.Find another way 2.Enter tunnel")
    user = int(input("Choose 1 or 2: "))
    if user == 1:
        print("You are not that smart")
    elif user == 2:
        print("You start to escape but your friend is to weak to go with you. They hand you a note.")
        print("What do you do?")
        print("1.Go back 2.Read the note")
        user = int(input("Choose 1 or 2: "))
        if user == 1:
            print("You are not that smart")
        elif user == 2:
            print("It is too dark to read the note.")
            print("What do you do?")
            print("1.Leave 2.Stay with friend")
            user = int(input("Choose 1 or 2: "))
            if user == 1:
                print("You crawl through the tunnel and the tunnel leads you to a beach")
                print("What do you do?")
                print("1.Run  2.Look around")
                user = int(input("Choose 1 or 2: "))
                if user == 1:
                    print("You are not that smart")
                elif user == 2:
                    print("In the water you see a boat")
                    print("What do you do?")
                    print("1.Get on the boat 2.Swim away")
                    user = int(input("Choose 1 or 2: "))
                    if user == 1:
                        print("Congratulations, you are heading to a new world!")
                    elif user == 2:
                        print("You are not that smart")
            elif user == 2:
                print("You are not that smart")
elif user == 2:
    print("You are not that smart")
else:
    print("Please Check your input")