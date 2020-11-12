def start():
    # give some prompts.
    print("\nYou're walking in the woods"
          "\nThere's no one around and your phone is dead"
          "\nOut of the corner of your eye you spot him:"
          "\nShia LaBeouf."
          "\nHe's following you, about 30 feet back"
          "\nHe gets down on all fours and breaks into a sprint"
          "\nHe's gaining on you"
          "\nShia LaBeouf")
    print("You can try to make your way to your car, or take on L. Which one do you take? (c or l)")

    # convert the player's input() to lower_case
    answer = input(">").lower()

    if "c" in answer:
        # if player typed "car" or "c" lead  to car_scene()
        car_scene()
    elif "l" in answer:
        game_over("You accept you fate and get devoured by your Hollywood hero Shia LaBeouf")
    else:
        # else call game_over() function with the "reason" argument
        game_over("Incorrect answer. Shia has created a temporal wormhole of awesomeness causing the game to reset")


def victory():
    print("Yes, you killed Shia LaBeouf. But now YOU must take his place."
          "\nTHE END???")
    play_again()


# function to ask play again or not
def play_again():
    print("\nDo you want to play again? (y or n)")

    # convert the player's input to lower_case
    answer = input(">").lower()

    if "y" in answer:
        # if player typed "yes" or "y" start the game from the beginning
        start()
    else:
        # if user types anything besides "yes" or "y", exit() the program
        exit()


# game_over function accepts an argument called "reason"
def game_over(reason):
    # print the "reason" in a new line (\n)
    print("\n" + reason)
    print("Game Over!")
    # ask player to play again or not by activating play_again() function
    play_again()


# diamond room
def forest_scene():
    # some prompts
    print("Now it's dark and you seem to have lost him"
          "\nBut you're hopelessly lost yourself"
          "\nStranded with a murderer"
          "\nYou creep silently through the underbrush"
          "\nAha! In the distance"
          "\nA small cottage with a light on"
          "\nHope!")
    print("What would you do? (1 or 2)"
          "\n1). Approach the cottage stealthily"
          "\n2). Look around for something, anything to help you.")

    # take input()
    answer = input(">")

    if answer == "1":
        # the player is dead, call game_over() function with the "reason"
        beartrap_scene()
    elif answer == "2":
        # the player won the game
        game_over("You stumble aimlessly through the woods, suddenly you feel a sharp pain on your neck"
                  "\nYou have just been decapitated by Shia LaBeouf!")
        # activate play_again() function
        play_again()
    else:
        # call game_over() with "reason"
        game_over("Incorrect answer. Shia has created a temporal wormhole of awesomeness causing the game to reset")


# monster room
def beartrap_scene():
    # some prompts
    # '\n' is to print the line in a new line
    print("You move stealthily toward it"
          "\nBut your leg! Ah! It's caught in a bear trap!")
    print("What would you do? (1 or 2)"
          "\n1). Gnaw off your leg"
          "\n2). Try to forcefully pry off the bear trap")

    # take input()
    answer = input(">")

    if answer == "1":
        # lead him to the diamond_room()
        print("Gnawing off your leg (Quiet, quiet)"
              "\nLimping to the cottage (Quiet, quiet)"
              "\nNow you're on the doorstep")
        cottage_scene()
    elif answer == "2":
        # the player is dead, call game_over() with "reason"
        game_over("You make too much rash movements. Your blood oozes and you die.")
    else:
        # game_over() with "reason"
        game_over("Incorrect answer. Shia has created a temporal wormhole of awesomeness causing the game to reset")


# bear room
def car_scene():
    # give some prompts
    # '\n' is to print the line in a new line
    print("You're looking for you car but you're all turned around"
          "\nHe's almost upon you now"
          "\nAnd you can see there's blood on his face"
          "\nMy God, there's blood everywhere!")
    print("\nWhat do you do? (1 or 2)")
    print("1). You sprint away into the woods.")
    print("2). Fight him.")

    # take input()
    answer = input(">")

    if answer == "1":
        # the player is dead!
        print("Running for you life (from Shia LaBeouf)"
              "\nHe's brandishing a knife (It's Shia LaBeouf)"
              "\nLurking in the shadows"
              "\nHollywood superstar Shia LaBeouf"
              "\nLiving in the woods (Shia LaBeouf)"
              "\nKilling for sport (Shia LaBeouf)"
              "\nEating all the bodies"
              "\nActual cannibal Shia LaBeouf")
        forest_scene()
    elif answer == "2":
        # lead him to the diamond_room()
        game_over("Unsurprisingly, Shia bites you and kills you"
                  "\nYou have just been digested by Shia LaBeouf")

    else:
        # else call game_over() function with the "reason" argument
        game_over("Incorrect answer. Shia has created a temporal wormhole of awesomeness causing the game to reset")


# template room
def cottage_scene():
    # some prompts
    # '\n' is to print the line in a new line
    print("Sitting inside: Shia LaBeouf"
          "\nSharpening an axe (Shia LaBeouf)"
          "\nBut he doesn't hear you enter (Shia LaBeouf)")
    print("What would you do? (1,2,...)"
          "\n1). Reason with Shia LaBeouf"
          "\n2). Assassinate Shia LaBeouf"
          "\n3). Run away")

    # take input()
    answer = input(">")

    if answer == "1":
        game_over("You speak out to Shia."
                  "\nHe throws his axe at you"
                  "\nYou fall to the floor and die")
    elif answer == "2":
        strangle_scene()
    elif answer == "3":
        game_over("The floor board creaks, and Shia attacks"
                  "\nYou have just been decapitate by Shia LaBeouf!")
    else:
        # game_over() with "reason"
        game_over("Incorrect answer. Shia has created a temporal wormhole of awesomeness causing the game to reset")


# template room
def strangle_scene():
    # some prompts
    # '\n' is to print the line in a new line
    print("Strangling superstar Shia LaBeouf"
          "\nFighting for your life with Shia LaBeouf"
          "\nWrestling a knife from Shia LaBeouf"
          "\nStab him in his kidney"
          "\nSafe at last from Shia LaBeouf")
    print("What would you do? (1,2,...)"
          "\n1). See if Shia is alive"
          "\n2). Run (limp) away from the scene")

    # take input()
    answer = input(">")

    if answer == "1":
        game_over("Wait! He isn't dead (Shia surprise)"
                  "\nThere's a jaw to your face"
                  "\nAnd death has arrived"
                  "\nYou have just been bitten by Shia LaBeouf")
    elif answer == "2":
        limp_scene()
    else:
        # game_over() with "reason"
        game_over("Incorrect answer. Shia has created a temporal wormhole of awesomeness causing the game to reset")


# template room
def limp_scene():
    # some prompts
    # '\n' is to print the line in a new line
    print("You limp into the dark woods"
          "\nBlood oozing from your stump leg"
          "\nBut you have won; you have beaten"
          "\nShia LaBeouf"
          "\n"
          "\nWait! He isn't dead (Shia surprise)"
          "\nThere's a gun to your head and death in his eyes")
    print("What would you do? (1 or 2)"
          "\n1). Use Jis Jitsu"
          "\n2). Run away")

    # take input()
    answer = input(">")

    if answer == "1":
        legendary_fight_scene()
    elif answer == "2":
        game_over("You cannot run away from the gunshot"
                  "\nYou have just been shot by Shia LaBeouf")
    else:
        # game_over() with "reason"
        game_over("Incorrect answer. Shia has created a temporal wormhole of awesomeness causing the game to reset")


# template room
def legendary_fight_scene():
    # some prompts
    # '\n' is to print the line in a new line
    print("But you can do Jis Jitsu"
          "\nBody slam superstar Shia LaBeouf"
          "\nLegendary fight with Shia LaBeouf"
          "\nNormal Tuesday night for Shia LaBeouf"
          "\nYou try to swing an axe at Shia Labeouf"
          "\nBut blood is draining fast from your stump leg"
          "\nHe's dodging every swipe, he parries to the left")
    print("What would you do? (1 or 2)"
          "\n1). Swing to to the right"
          "\n2). Swing to to the left")

    # take input()
    answer = input(">")

    if answer == "1":
        victory_scene()
    elif answer == "2":
        game_over("You counter to the left, he counters you in the shin"
                  "\nYou topple to the floor, colourless."
                  "\nShia has won")
    else:
        # game_over() with "reason"
        game_over("Incorrect answer. Shia has created a temporal wormhole of awesomeness causing the game to reset")


# template room
def victory_scene():
    # some prompts
    # '\n' is to print the line in a new line
    print("You counter to the right, you catch him in the neck"
          "\nYou're chopping his head now"
          "\nYou have just decapitated Shia Labeouf"
          "\n"
          "\nHis head topples to the floor, expressionless"
          "\nYou fall to your knees and catch your breath"
          "\nYou're finally safe from Shia LaBeouf ...")
    victory()


# start the game
start()
