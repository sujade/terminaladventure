print("         _                  \n"
      "       _|=|__________       \n"
      "      /              \      \n"
      "     /                \     \n"
      "    /__________________\    \n"
      "     ||  || /--\ ||  ||     \n"
      "     ||[]|| | .| ||[]||     \n"
      "   ()||__||_|__|_||__||()   \n"
      "  ( )|-|-|-|====|-|-|-|( )  \n"
      "  ^^^^^^^^^^====^^^^^^^^^^^ ")

print(" ")

print("============================\n"
      "  Lost in the Witch House   \n"
      "============================")

print(" ")

answer = input("You are in a dark room in a mysterious house.\n"
               "In front of you, you see a door in the dark. You can't see anything else.\n"
               "The air smalls like mold and you can hear scratching noises coming somewhere above.\n"
               "You reach for the door and it opens with a loud creak.\n"
               "You see a long hallway with two doors on both sides.\n"
               "Which door do you choose? (left/right)")

if answer == "left":
    print("The door opens with a creak and you see a dark room filled with old furniture.\n"
          "There is a mirror on the wall that's dusty and cracked.\n"
          "Deciding to be brave, you wipe off the dust.\n"
          "You see someone in the mirror. It's you, but not you.\n"
          "In terror, you turn around and try opening the door, but it won't budge.\n"
          "Trapped in the room, you hear faint whispers in the dark surrounding you slowly.\n"
          "You feel a cold hand on your shoulder and you scream.\n"
          "Another victim for the Witch House.\n"
          "GAME OVER")
    exit()

elif answer == "right":
    print("The door opens with a creek and you see a staircase leading down.\n"
          "You decide to go down the stairs.\n"
          "At the bottom it's a big room with a fireplace and a table.\n"
          "There is a flashlight on the table.\n"
          "You take the flashlight and turn it on. If lets out a faint light.\n"
          "The room you can see better now is filled with old furniture and cobwebs.\n"
          "On the other side of the room, there is a door.\n"
          "You take hesitant towards the door and open it.\n"
          "This room is way smaller, and has a small desk with a candle on and a key.\n")

    answer = input("Do you take the key? (yes/no)")
    if answer == "yes":
        print("You reach for the key with your shaking hands and hold onto it.\n"
              "Deciding to leave the room, you go back to the previous room.\n"
              "There is a door that wasn't there in this room before...\n"
              "Your steps are hasty and clumsy, you reach for the door and unlock it.\n"
              "This room is cold.\n"
              "The door behind you slams shut and you hear a faint laughter.\n"
              "You will rot in this room.\n"
              "GAME OVER")
        exit()
    elif answer == "no":
        print("Your hands are hasty on your keyboard, trying to finish this little Python game.\n"
              "It's not too different from the others, nothing standing out.\n"
              "Why didn't you take the key?\n")
        answer = input("Do you take the key? (yes/no)")
        if answer == "yes":
            print("Good... The key is all yours.\n"
                  "You'll stay in this house forever.\n"
                  "GAME OVER")
            exit()
        elif answer == "no":
            print("But you can't leave without it...\n")
        answer = input("Do you take the key? (yes/no)")
        if answer == "yes":
            print("Good... The key is all yours.\n"
                  "You'll stay in this house forever.\n"
                  "GAME OVER")
            exit()
        elif answer == "no":
            print("TAKE. THE. DAMN. KEY!\n")
        answer = input("Do you take the key? (yes/no)")
        if answer == "yes":
            print("Good... The key is all yours.\n"
                  "You'll stay in this house forever.\n"
                  "GAME OVER")
            exit()
        elif answer == "no":
            print("You are a stubborn one...\n"
                  "Good. Time for you to go.\n"
                  "The door opens behind your back.\n"
                  "YOU'RE FREE!")
