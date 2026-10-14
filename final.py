#EE, IA, CL, KT The Game Final
#IA

with open ('inventory.txt', 'r') as file:
    inventory = file.read()

choices = []
gems = 0
inventory = []
yellow_gem = "yellow gem"
green_gem = "green gem"
blue_gem = "blue gem"
gem_piece = 0
choices = []
keys = 0

def duo_choice(key, door):
    while True:
        puzzle2 = input("What key do you put in what door. Type as (key, door): ").lower()
        if puzzle2 == f"{key}, {door}" and f"{door}" not in choices:
            print("Thats right.")
            keys += 1
            choices.append(f"{door}")
            if keys == 6:
                print("All the doors open and in the black one, is a piece of a blue gem.")
                gem_piece += 1
                break
            else:
                continue
        else:
            print("That is wrong, you see all the keys disappear and reappear back on the table.")
            keys = 0
            choices = []
            continue
    return puzzle2

print('You wake up on a table with four different doors but one door has three colored\ngem shaped divots on it. The first divot is brown, the second is green and the\nthird is blue. All of the other doors are different colors with different titles\non it. The first door has cheetah print on it with a title that says "past".\nThe second door is green with a title that says "present". The third door is\nblue with a title that says "future". You need to collect the gems from each\nroom inorder to unlock the main door to get the treasure behind it.')
                               
while True:
    door = input("Type title of door you want to go into: ").lower()
    if door == "past":
        print("You are now in the past. Find the hidden gem to escape.")
    elif door == "present":
        print("You are now in the present. Defeat the boss to collect the gem")
        break
    elif door == "future":
        print("You are now in the future. You are in a room that has three doors, one rustic, on silver, and one gold.")
        break
    else:
        print("Type in one of the titles")
        continue

def have_gem(gem):
    if gem in inventory:
        print("You are back in the main room.")
        print(f"The {gem} fly's from your hand and goes into its colored divot.")
        print(door)
    else:
        print("You need to find the gem to exit this time line.")
    return gem 

#KT


places = 0
if door == "past":
    pickaxe = "pickaxe"
    direction = input("You have 3 choices where do you want to go? (Cave, Forest, Volcano): ").title()


if door == "past":
    pickaxe = "pickaxe"
    direction = input("You have 3 choices where do you want to go? (Cave, Forest, Volcano): ").title()
    direction = input("You have 3 choices where do you want to go? (Cave, Forest, Volcano): ").title()
    restart = ("you lost. restart past.")
    while True:
        print(direction)
        while direction == "Cave":
            places += 1

            print("You chose cave. around you you see glowing crystals tucked into the rocks, and when you turn a corner you see a huge flowing waterfall, stalactites hang from above. Bright green moss cover the walls along with tall leafy plants with vibrant cherry red flowers.")
       
            print("You chose cave. around you you see glowing crystals tucked into the rocks, and when you turn a corner you see a huge flowing waterfall, stalactites hang from above. Bright green moss cover the walls along with tall leafy plants with vibrant cherry red flowers.")
        
            look = input("you have 3 choices where do you want to look first (Waterfall, Cavemen Art, Steam Vents ): ").lower()
            print(look)
            if look == "waterfall":
                waterfall = (input("Do you want to look in the (Pool) of water or (Behind) the waterfall?:")).lower()
                print(waterfall)
                if waterfall == "pool":
                    print("you swim with the fishes. nothings there, go somewhere else.")
                    print(look)   
                    print(look)
                elif waterfall == "behind":
                    print("you get soaked. All you see is a measly pile of gold but you leave it there because you don't want it.")
                    print(look)
            elif look == "steam vents":
                print("the hot steam shoots up from the vents. you get burned.")
                print(restart)
                print(direction)
                   
            elif look ==  "cavemen art":
                print("A bright golden crystal shines hidden in the eye of the painting. Use the pickaxe from your inventory to collect.")
                if pickaxe not in inventory:
                    no_pickaxe = (input("go to another room to find the pickaxe (Forest, Volcano):")).title()
                    if no_pickaxe == "Forest":
                        direction = "Forest"
                
                
                    elif no_pickaxe == "Volcano":
                        direction = "Volcano"
                elif pickaxe in inventory:
                    next_door = (input("You have collected the yellow gem go back to the main room to go through a different door, type (ok):")).lower
                    inventory.append("yellow_gem")
                    if next_door == "ok":
                        print(door)
        while direction == "Forest":
            view = input("Where do you want to look first? (Nesting Ground, Tar Pit, Swamp: )").title()
            print(f"you chose Forest. a bright blue and pink sky blankets over you. tall, luscious trees loom above. {view}")
            print(direction)
            print(direction)
        while direction == "Forest":
            
            print(input("you chose Forest. a bright blue and pink sky blankets over you. tall, luscious trees loom above."))
           
            view = input("Where do you want to look first? (Nesting Ground, Tar Pit, Swamp").title()
            print(view)
            if view == "Nesting Ground":
                reaction = (input("You're at the dinosaur nesting grounds. you step on one of the eggs and a tyrannosaurus appears, angry. what will you do? (fight, run):")).lower
                if reaction == "fight":
                    print("When you fight the dino you almost die. But last minute you throw a stick and it gets stuck in its eye. You win!")
                    print("Collect your reward! you have received a pickaxe. Now you will be able to collect your gem.")
                    inventory.append(pickaxe)
                    print(direction)
                elif reaction == "run":
                    print("You get so scared you run away. while you're running you trip on a root and fall into a nest, crushing 3 more eggs when you land. the tyrannosaurus gets even more angry. Sadly you die.")
                    print(restart)
                    print(direction)
            elif view == "Tar Pit":
                print("oooh, wrong choice. When you go to the tar pits you fall in. so sad. you die.")
                print(restart)
                print(direction)
            elif view == "Swamp":
                options = ("when you get to the swamp will you (go in water) or (jump across) the logs:").lower()
                print(options)
                if options == "go in water": 
                    if options == "go in water":
                        print("when you go in the water you get a severe bacteria infection.")
                    print(restart)
                    print(direction)
                elif options == "jump accross":
                    print("you thought those were logs? there actually really hungry Deinosuchus (basically an alligator)")
                    print(restart)
                    print(direction)

        while direction == "Volcano":
            area = input("you've reached the volcano. where do you want to go? (Pumice Pit, Magma River):").title()
            print(area)
            if area == "Pumice Pit":
                print("The deep ash pits were camouflaging raptor nests. One of them comes flying down and snatches you, it drops you off in the volcano.")
                print (restart)
                print(direction)
            elif area == "Magma River":
                print("you try to cross the flowing river of magma, but unfortunately your foot slips.")
                print(restart)
                print(direction)
        have_gem(yellow_gem)



#EE
directions = 0
revolver = "revolver"
Restart = ("you lost. restart present")
if door == "present":
    while True:
        place = input("You have 3 choices where do you want to go?: Oval Office, Lincoln Monument, National Art Gallery:").title()
        if place == "Oval Office":
            directions += 1 
           
            print("you chose oval office. around you you see an oval shaped room with a large desk, paintings, and american flags find a revolver to get the gem. *hint: you might find it in the other choices")
            looks = input("you have 3 choices where do you want to look first (Desk, Paintings, Flags ): ").lower() 
            
            print(looks)

            if looks == "Desk":
                print("You search through the desk and find important papers and old documents.Nothing else is there.")

            elif looks == "Paintings":
                print ("You examine the presidential portaits and discover a hidden message pointing toward the Lincoln Monument.")
            elif looks == "Flags":
                print("You look behind the American flags and find nothing.")
            place = input("Where do you want to go next? (Oval Office, Lincoln Monumnet, National Art Gallery: "). title()

        elif place == "Lincoln Monument":
            directions += 1

            print ("You chose the Lincoln Monument. A giant statue of Abraham Lincoln sits above you, surrounded by tall marble columns.")

            looks = input("Where do you want to look first? (Statue, Steps, Columns): ").title()

            if looks == "Statue":
                print("You look behind the statue and discover a hidden revolver!")

                if revolver not in inventory:
                    inventory.append(revolver)
                    print("You collected the revolver! You can now defend yourself at the National Art Gallery.")
                else:
                    print("You already have the revolver.")

            elif looks == "Steps":
                print("You search the marble steps and find an old note about a secret room in the National Art Gallery.")
            elif looks == "Columns":
                print("You looks behind the columns and discover a map showing the way to the Natinal Art Gallert.")
            place = input("Where do you want to go next? (Oval Office, Lincoln Monument, National Art Gallery):").title()

        elif place == "National Art Gallery":
            directions += 1
            
            print("You enter the National Art Gallery. Paintings and sculptures fill the halls. Suddenly, Trump appears and guards a glowing green gem!")

            if revolver not in inventory:
                print("You don't have a revolver, so you aren't ready for the challenge.")
                print("Go to the Lincoln Monument to find one!")
                place = input("Where do you want to go? (Oval Office, Lincoln Monument, National Art Gallery):")
            else:
                fight = input("Trump blocks your path to the green gem! Do you want to (Fight) or (Run)?:").title()

                if fight == "Fight":
                    print("You use your revolver to defend yourself and defeat Trump!")
                    print("You approach the glowing green gem and collect it!")

                if green_gem not in inventory:
                    inventory.append(green_gem)
                    gems += 1
                else:
                    print("You already collected the green gem.")
                    if fight == "Run":
                        print("You run away from the challenge. You lose your chance to collect the gem.")
                        print(Restart)    
                    else:
                        print("That is not a valid choice.")

                        place = "National Art Gallery"
                        print("That is not a valid location.")
                        place = input("Where do you want to go? (Oval Office , Lincoln Monument, National Art Gallery):").title()
                    have_gem(green_gem)
#CL
if door == "future":
    room = input("What room do want to go to: ").lower()
    if room == "rustic":
        print("You are in a room with a (1)computer, (2)lamp, (3,4,5)desk with three drawers, (6)bed, (7)chair, and a (8)safe with three underscores blinking.")
        while True:
            puzzle1 = input("What do you check: ")
            if puzzle1.isalpha():
                print("Type your choice as a number shown for your choice")
            else:
                if puzzle1 == 4:
                    print("You see '__9'.")
                    continue
                elif puzzle1 == 1:
                    print("You break apart the computer and behind the mother drive you see '3__'.")
                    continue
                elif puzzle1 == 2:
                    print("You found nothing")
                    continue
                elif puzzle1 == 3:
                    print("You found nothing")
                    continue
                elif puzzle1 == 5:
                    print("You found nothing")
                    continue
                elif puzzle1 == 6:
                    print("You see '_7_'")
                    continue
                elif puzzle1 == 7:
                    print("You found nothing")
                    continue
                elif puzzle1 == 8:
                    code = input("Type in code: ")
                    if code == 379:
                        print("Correct, in the safe you find a broken piece of a blue gem.")
                        gem_piece += 1
                        print("You leave back to the first room")
                        print(room)
                    else:
                        print("That is incorrect.")
                        continue
            if gem_piece == 2:
                inventory.append("blue_gem")
                print("You now have the blue gem.")
    elif room == "silver":
        print("You are in a room with six different keys on a table and six different doors, one key is red, one is orange, one is yellow, one is green, one is blue, and on is purple. One door is yellow, one is tan, one is black, one is green, one is blue, and one is cyan. This puzzle is pretty easy even when your BLIND.")
        duo_choice("red", "black")
        duo_choice("orange", "tan")
        duo_choice("yellow", "green")
        duo_choice("green", "yellow")
        duo_choice("blue", "cyan")
        duo_choice("purple", "blue")
        if gem_piece == 2:
            inventory.append("blue_gem")
            gems += 1
            print("You now have the blue gem")
            print(door)
    elif room == "gold":
        print("You die from falling into lava, you respawn at the beginning of future")
        print(room)
        choices = []
        key = 0
        gem_piece = 0
    else:
        print("That isn't one of the rooms")
        print(room)
    have_gem("blue_gem")

if  gems == 3:
    print("You're back in the main room and have escaped! Congragulations")