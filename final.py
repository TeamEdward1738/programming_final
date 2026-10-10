#EE, IA, CL, KT The Game Final

choices = []
gems = []
inventory = []
with open ("inventory.txt","r") as file:
#    content = file.read()
#    inventory = idk fix this later

# IA  

print('You wake up on a table with four different doors but one door has three colored\ngem shaped divots on it. The first divot is yelloe, the second is green and the\nthird is blue. All of the other doors are different colors with different titles\non it. The first door has cheetah print on it with a title that says "past".\nThe second door is green with a title that says "present". The third door is\nblue with a title that says "future". You need to collect the gems from each\nroom inorder to unlock the main door to get the treasure behind it.')


while True:
    door  = input(f"Type title of door you want to go into: ").lower()
    if door == "past":
        print("You are now in the past. Find the pickaxe to mine the hidden gem to escape.")
    elif door == "present":
        print("You are now in the present. Defeat the boss to collect the gem")
    elif door == "future":
        print("You are now in the future. You look around and see tall silver walls all around you and see a path down and a bunch of left turns and right turns.")
    else:
        print("You need to type in one of the titles!")
        continue
    break

#KT
if door == "past":
    pickaxe = "pickaxe"
    direction = input("You have 3 choices where do you want to go? (Cave, Forest, Volcano): ").tittle()
    restart = ("you lost. restart past.")
    while True:
        print(direction)
        while direction == "Cave":
            places += 1

            print("You chose cave. around you you see glowing crystals tucked into the rocks, and when you turn a corner you see a huge flowing waterfall, stalactites hang from above. Bright green moss cover the walls along with tall leafy plants with vibrant cherry red flowers.")
        
            look = input("you have 3 choices where do you want to look first (Waterfall, Cavemen Art, Steam Vents ): ").lower()
            print(look)
            if look == "waterfall":
                waterfall = (input("Do you want to look in the (Pool) of water or (Behind) the waterfall?:")).lower()
                print(waterfall)
                if waterfall == "pool":
                    print("you swim with the fishes. nothings there, go somewhere else.")
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
                    gem += 1
                    if next_door == "ok":
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
                    print("when you go in the water you get a severe bacteria infection.")
                    print(restart)
                    print(direction)
                elif options == "jump accross":
                    print("you thought those were logs? there actually really hungry Deinosuchus (basically an alligator)")
                    print(restart)
                    print(direction)

        while direction == "Volcano":
            area = input("you've reached the volcano. where do you want to go? (Pumice Pit, Magma River)").title()
            print(area)
            if area == "pumice pits":
                print("The deep ash pits were camouflaging raptor nests. One of them comes flying down and snatches you, it drops you off in the volcano.")
                print (restart)
                print(direction)
            elif area == "Magma Rive":
                print("you try to cross the flowing river of magma, but unfortunately your foot slips.")
                print(restart)
                print(direction)

#EE
if door == "present":
   revolver= "revolver"
   place=input("You have 3 choices where do you want to go?: Oval Office, Lincoln Monument, National Art Gallery")

   if place == "Oval Office":
      print("you chose oval office. around you you see find a revolver to get the gem. *hint: you might find it in the other choices")
#CL
if door == "future":
    computer = 1
    lamp = 2
    top_drawer = 3
    middle_drawer = 4
    bottom_drawer = 5
    bed = 6
    chair = 7
    not_checked = [1,2,3,4,5,6,7]
    nothing = "You found nothing"
    while True:
        decition1 = input(f"You come to your first decition, left, right, or forward. What do you choose: ").lower()
        if decition1 == "left":
            while True:
                decition11 = input("You come to a left or right decition. What do you choose: ").lower()
                if decition11 == "left":
                    while True:
                        decition111 = input("You come to a left or right decition. What do you choose: ").lower()
                        if decition111 == "left":
                            print("You are in a room with a (1)computer, (2)lamp, (3,4,5)desk with three drawers, (6)bed, (7)chair, and a (8)safe with three underscores blinking.")
                            while True:
                                puzzle1 = input("What do you check: ")
                                if puzzle1.isnumeric():
                                    if puzzle1 in not_checked:
                                        if puzzle1 == 4:
                                            print("You see '__9'.")
                                            continue
                                        elif puzzle1 == 1:
                                            print("You break apart the computer and behind the mother drive you see '3__'.")
                                            continue
                                        elif puzzle1 == 2:
                                            print(nothing)
                                            continue
                                else:
                                    print("Type in your choice as the number shown.")
                                    continue