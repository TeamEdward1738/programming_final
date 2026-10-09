#EE, IA, CL, KT The Game Final

choices = []
gems = []
inventory = []

# IA  

print('You wake up on a table with four different doors but one door has three colored\ngem shaped divots on it. The first divot is brown, the second is green and the\nthird is blue. All of the other doors are different colors with different titles\non it. The first door has cheetah print on it with a title that says "past".\nThe second door is green with a title that says "present". The third door is\nblue with a title that says "future". You need to collect the gems from each\nroom inorder to unlock the main door to get the treasure behind it.')


while True:
    door  = input(f"Type title of door you want to go into: ").lower()
    if door == "past":
        print("You are now in the past. Find the hidden gem to escape.")
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
    direction = input("You have 3 choices where do you want to go? (Cave, Forest, ): ").capitalize()

    if direction == "Cave":
        print("you chose cave. around you you see glowing crystals tucked into the rock, and when you turn a corner you see a huge flowing waterfall, stalagtites hang from above. Bright green moss covers the walls along with tall leafy plants with vibrant cherry red flowers. find a pickaxe to get the gem. *hint: you might find it in the other choices.")
        if pickaxe in inventory:
            look = input("you have 3 choices where do you want to look first (Waterfall, walls, plants): ").lower()
            if look == "waterfall":
                print("You see gem")
    elif direction == "Forest":
        print()
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