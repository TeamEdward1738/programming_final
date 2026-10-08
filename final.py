#EE, IA, CL, KT The Game Final

print('You wake up on a table with four different doors but one door has three colored gem shaped divots\n on it. The first divot is brown, the second is green and the third is blue. All of the other doors are different colors with different titles on it.\nThe first door has cheetah print on it with a title that says "past". The\nsecond door is green with a title that says "present". The third door is\nblue with a title that says "future". You need to collect the gems from\neach room inorder to unlock the main door to get the trausure behind it.')

choices = []

while True:
    choice  = input(f"Type title of door you want to go into: ").lower()
    if choice == "past":
        print("You are now in the past. Find the hidden gem to escape.")
    elif choice == "present":
        print("You are now in the present. Defeat the boss to collect the gem")
    elif choice == "future":
        print("You are now in the future. Find the hidden gem to escape and unlock one of the ")
    else:
        print("You need to type in one of the titles!")
        continue
    break

#IA




#KT




#EE




#CL
