def main():
    
    answer = input("Wpuld you like to play the game? (yes/no) ")
    while answer != "yes" and answer != "no":
        answer = input("Please enter (yes/no) ")

    if answer.lower().strip() == "yes":
        answer = input("You reach a crossroads, would you like to go left or right? (left/right) ").lower().strip()
        while answer != "left" and answer != "right":
            answer = input("Please enter (left/right) ")

            # left
            if answer == "left":
                answer = input("You encounter a werewolf, would you like to run or attack? (run/attack) ")
                while answer != "run" and answer != "attack":
                   answer = input("Please enter (run/attack) ")

                if answer == "run":
                    print("That was not the greatest idea. You lost :[")
                else:
                    print("Great choice, you defeated the werewolf!")

                    answer = input("You see a car and a plane. Which wone would you like to take? (car/plane) ").lower().strip()
                    while answer != "car" and answer != "plane":
                        answer = input("Please enter (car/plane) ")

                    if answer == "plane":
                        print("Unfortunately, you don't know how to fly one. Game over! :[ ")
                    else:
                        print("Yay, you made it safely! :] ")

        # right
        if answer == "right":
            answer = input("You encounter a huge castle. You you like to enter or continue walking? (enter/walk) ").lower().strip()
            while answer != "enter" and answer != "walk":
                answer = input("Please enter (enter/walk) ")

            if answer == "enter":
                print("You enter and see a witch making a potion. She offers you two choices, either you take the potion and become immortal or she gives you powers to make it safely out of the forest.")

                answer = input("Which choice will you take? (potion/power) ")
                while answer != "potion" and answer != "power":
                    answer = input("Please enter (potion/power) ")

                if answer == "potion":
                    print("Oh poor thing, the portion was too string for you. Game over :[")
                else:
                    print("Great choice, you left and made it safely! :]")
            else:
                print("You continue walking and encounter plum apples. ")

                answer = input("Would you like to eat them? (yes/no) ")
                while answer != "yes" and answer != "no":
                    answer = input("Please enter (yes/no) ")

                if answer == "yes":
                    print("Oh they were poisonous! You died :[ Game Over! ")
                else: 
                    print("Great choice! Those apples were fatal! ")

                    answer = input("Ahead, you see a car and a plane. WHich wone would you like to take? (car/plane) ")
                    while answer != "car" and answer != "plane":
                        answer = input("Please enter (car/plane) ")

                    if answer == "plane":
                        print("Unfortunately, you don't know how to fly one. :[ Game over ")
                    else:
                        print("Yay, you made it safely! :] ")

    else:
        print("That's bad, you lost. :[ ")

if __name__ == '__main__':
    main()