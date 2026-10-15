#EE, IA, KT, CL Game FInal

inventory = []

yellow_gem = "yellow gem"
green_gem = "green gem"
blue_gem = "blue gem"
revolver = "revolver"
pickaxe = "pickaxe"

gems = 0
gem_piece = 0
keys = 0
choices = []


def have_gem(gem):
    if gem in inventory:
        print("You are back in the main room.")
        print(f"The {gem} flies from your hand into its colored divot.")
    else:
        print("You need to find the gem to exit this timeline.")
    return gem


def check_blue_gem():
    global gem_piece

    if gem_piece >= 2 and blue_gem not in inventory:
        inventory.append(blue_gem)
        print("You now have the blue gem!")


def duo_choice(key, door):
    global keys, gem_piece

    puzzle2 = input(f"What key goes in what door? Type as (key, door): ").lower().strip()

    if puzzle2 == f"{key}, {door}" and door not in choices:
        print("That's right.")
        keys += 1
        choices.append(door)

        if keys == 6:
            print("All the doors open! You find a piece of a blue gem.")
            gem_piece += 1
    else:
        print("Wrong! The keys disappear and return to the table.")
        keys = 0
        choices.clear()


#KT PAST TIMELINE
def past_timeline():
    print("You are now in the past. Find the hidden gem to escape.")

    while True:
        direction = input("Where do you want to go? (Cave, Forest, Volcano): ").strip().title()

        if direction == "Cave":
            print("You chose the cave. Glowing crystals are tucked into the rocks. A waterfall flows nearby, stalactites hang above, and bright green moss and red flowers cover the walls.")

            look = input("Where do you want to look? (Waterfall, Cavemen Art, Steam Vents): ").strip().lower()

            if look == "waterfall":
                waterfall = input("Look in the (pool) of water or (behind) the waterfall? ").strip().lower()

                if waterfall == "pool":
                    print("You swim with the fishes. Nothing is there.")

                elif waterfall == "behind":
                    print("You get soaked. You find gold but leave it there.")

                else:
                    print("Invalid choice.")

            elif look == "steam vents":
                print("Hot steam shoots from the vents. You get burned.")
                print("You lost this attempt.")

            elif look == "cavemen art":
                print("A bright golden crystal shines in the eye of the painting.")

                if pickaxe not in inventory:
                    print("You need a pickaxe. Find one in the Forest.")

                else:
                    print("You use the pickaxe to collect the yellow gem.")

                    if yellow_gem not in inventory:
                        inventory.append(yellow_gem)

                    have_gem(yellow_gem)
                    return

            else:
                print("That is not one of the choices.")

        elif direction == "Forest":
            view = input("Where do you want to look? (Nesting Ground, Tar Pit, Swamp): ").strip().title()

            if view == "Nesting Ground":
                reaction = input("A tyrannosaurus appears. Do you (fight) or (run)? ").strip().lower()

                if reaction == "fight":
                    print("You throw a stick, it gets stuck in the dinosaur's eye, and you win!")
                    print("You receive a pickaxe.")

                    if pickaxe not in inventory:
                        inventory.append(pickaxe)

                elif reaction == "run":
                    print("You run away. You lost this attempt.")

                else:
                    print("Invalid choice.")

            elif view == "Tar Pit":
                print("You fall into the tar pit. You lost this attempt.")

            elif view == "Swamp":
                options = input("Will you (go in water) or (jump across) the logs? ").strip().lower()

                if options == "go in water":
                    print("You get a severe bacterial infection. You lost this attempt.")

                elif options in ("jump across, jump across the logs"):
                    print("Those aren't logs! They're hungry Deinosuchus.")

                else:
                    print("Invalid choice.")

            else:
                print("That is not one of the choices.")

        elif direction == "Volcano":
            area = input("You reach the volcano. Where do you go? (Pumice Pit, Magma River): ").strip().title()

            if area == "Pumice Pit":
                print("Raptors snatch you from the ash pit. You lost this attempt.")

            elif area == "Magma River":
                print("You slip while crossing the magma river. You lost this attempt.")

            else:
                print("That is not one of the choices.")

        else:
            print("Type Cave, Forest, or Volcano.")


#  EE PRESENT TIMELINE
def present_timeline():
    print("You are now in the present. Defeat the boss to collect the gem.")

    while True:
        place = input("Where do you want to go? Oval Office, Lincoln Monument, National Art Gallery: ").strip().title()

        if place == "Oval Office":
            print("You see an oval-shaped room with a large desk, paintings, and American flags. Find a revolver to get the gem.")

            looks = input(
                "Where do you look? (Desk, Paintings, Flags): ").strip().lower()

            if looks == "desk":
                print("You find important papers and old documents, but nothing else.")

            elif looks == "paintings":
                print("A hidden message points toward the Lincoln Monument.")

            elif looks == "flags":
                print("You look behind the flags and find nothing.")

            else:
                print("That is not one of the choices.")

        elif place == "Lincoln Monument":
            print("A giant statue of Abraham Lincoln stands among ""tall marble columns.")

            looks = input("Where do you look? (Statue, Steps, Columns): ").strip().title()

            if looks == "Statue":
                if revolver not in inventory:
                    inventory.append(revolver)
                    print("You find and collect a revolver!")

                else:
                    print("You already have the revolver.")

            elif looks == "Steps":
                print("You find a note about a secret room in the National Art Gallery.")

            elif looks == "Columns":
                print("You find a map showing the way to the National Art Gallery.")

            else:
                print("That is not one of the choices.")

        elif place == "National Art Gallery":
            print("You enter the National Art Gallery.Trump guards a glowing green gem.")

            if revolver not in inventory:
                print("You don't have a revolver. Go to the Lincoln Monument to find one.")
                continue

            fight = input("Do you want to (Fight) or (Run)? ").strip().title()

            if fight == "Fight":
                print("You use your revolver to defeat the boss and collect the green gem!")

                if green_gem not in inventory:
                    inventory.append(green_gem)
                else:
                    print("You already collected the green gem.")

                have_gem(green_gem)
                return

            elif fight == "Run":
                print("You run away without collecting the gem.")

            else:
                print("That is not a valid choice.")

        else:
            print("That is not a valid location.")


#  CL FUTURE TIMELINE
def future_timeline():
    global gem_piece, keys, choices

    print("You are now in the future. Choose a room: Rustic, Silver, or Gold.")

    room = input("What room do you want to go to? ").strip().lower()

    if room == "rustic":
        print("The room has a (1) computer, (2) lamp, (3, 4, 5) desk drawers, (6) bed, (7) chair, and an (8) safe with a three-digit code.")

        clues_found = set()

        while True:
            puzzle1 = input("What do you check? (1-8, or leave): ").strip()

            if puzzle1 == "leave":
                return

            if puzzle1 not in ("1", "2", "3", "4", "5", "6", "7", "8"):
                print("Type a number from 1 to 8, or type leave.")
                continue

            if puzzle1 == "4":
                print("You see '__9'.")
                clues_found.add("9")

            elif puzzle1 == "1":
                print("Behind the computer's hard drive, you see '3__'.")
                clues_found.add("3")

            elif puzzle1 == "2":
                print("You find nothing.")

            elif puzzle1 == "3":
                print("You find nothing.")

            elif puzzle1 == "5":
                print("You find nothing.")

            elif puzzle1 == "6":
                print("You see '_7_'.")
                clues_found.add("7")

            elif puzzle1 == "7":
                print("You find nothing.")

            elif puzzle1 == "8":
                code = input("Type in the code: ").strip()

                if code == "379" and len(clues_found) == 3:
                    print("Correct! You find a broken piece of a blue gem.")
                    gem_piece += 1
                    check_blue_gem()
                    print("You return to the main room.")
                    return

                else:
                    print("That is incorrect, or you haven't found all clues.")

    elif room == "silver":
        print("Match the six keys to the doors. The pairs are: one red key, one orange key, one yellow key, one green key, one blue key, one purple key, one black door, one tan door, one green door, one yellow door, one cyan door, one blue door.")

        keys = 0
        choices = []

        pairs = [("red", "black"),("orange", "tan"),("yellow", "green"),("green", "yellow"),("blue", "cyan"),("purple", "blue")]

        for key, door_name in pairs:
            duo_choice(key, door_name)

            if keys == 0:
                print("The puzzle reset. Try the silver room again.")
                return

        print("You solved the puzzle and found a piece of a blue gem.")
        gem_piece += 1
        check_blue_gem()

    elif room == "gold":
        print("You die from falling into lava and respawn at the beginning of the future.")

        gem_piece = 0
        keys = 0
        choices = []

    else:
        print("That isn't one of the rooms.")

print('You wake up on a table with four different doors, but one door has three colored gem-shaped divots on it. The first divot is brown, the second is green, and the third is blue. All of the other doors are different colors with different titles on them. The first door has cheetah print on it with a title that says "past". The second door is green with a title that says "present". The third door is blue with a title that says "future". You need to collect the gems from each room in order to unlock the main door to get the treasure.')


while True:
    door = input("Which door do you enter? (Past, Present, Future, or Quit): ").strip().lower()

    if door == "past":
        past_timeline()

    elif door == "present":
        present_timeline()

    elif door == "future":
        future_timeline()

    elif door == "quit":
        print("Thanks for playing!")
        break

    else:
        print("Type past, present, future, or quit.")

    print("\nInventory:", inventory)

    if all(
        gem in inventory
        for gem in (yellow_gem, green_gem, blue_gem)
    ):
        print("You have all three gems!")
        print("The main treasure door unlocks.")
        print("Congratulations! You found the treasure!")
        break

