from time import sleep

# Game variables
Location = 0
hasShovel = False
hasKey = False
isGameRunning = True

print("Welcome to my very short text game! ^^")
sleep(1)
print("Would you like to play? Y/N ")

# input() stops the running code and waits for player input in the terminal.
# If input() is assigned to a variable, whatever the player typed in will be stored in that variable.
Input = input()
# Strings have a function `lower()`, which makes all characters in the string lowercase.
if Input.lower() == "y":
    print("Great!")

    # While loops run as long as the statement inside of them is true, once it's false the loop stops.
    while isGameRunning is True:
        # These if statements will run when the player is in their location.
        if Location == 0:
            print("You are at some unknown place in the middle of nowhere.")
            sleep(1)
            print("To your left is a patch of dirt, to your right is a pile of tools, and in front of you is a door...")
            sleep(1)

            # Action is a local variable taking an input.
            Action = input("Where do you go? Left/Right/Forward ")
            if Action.lower() == "left":
                # If we go left, set out location to 1.
                Location = 1
                sleep(1)
            elif Action.lower() == "right":
                # If we go right, set our location to 2.
                Location = 2
                sleep(1)
            elif Action.lower() == "forward":
                # And if we go forward, set our location to 3.
                Location = 3
                sleep(1)
        elif Location == 1:
            print("You see a patch of dirt.")
            sleep(1)
            Action = input("Dig it up? Y/N ")
            if Action.lower() == "y":
                if hasShovel is True:
                    # Make sure the player can only get the key if the player has the shovel.
                    print("You found a key!")
                    hasKey = True
                    # Set our location back to the beginning.
                    Location = 0
                    sleep(1)
                else:
                    # Do this if the player doesn't have the shovel...
                    print("There's too much dirt here, maybe you should try finding a shovel first...")
                    Location = 0
                    sleep(1)
            elif Action.lower() == "n":
                print("Maybe come back to it later...")
                Location = 0
        elif Location == 2:
            print("You found a shovel in the pile of tools!")
            sleep(1)
            Action = input("Take the shovel? Y/N ")
            if Action.lower() == "y":
                # Add the shovel to our "Inventory".
                print("You took the shovel!")
                hasShovel = True
                Location = 0
                sleep(1)
            elif Action.lower() == "n":
                print("You put the shovel down.")
                Location = 0
                sleep(1)
        elif Location == 3:
            print("You found a door, but it's locked...")
            sleep(0.5)
            Action = input("Try to open it? Y/N ")
            if Action.lower() == "y":
                if hasKey is True:
                    # Let the player win if they have the key.
                    print("You won!")
                    isGameRunning = False
                    sleep(1)
                else:
                    # Stop the player from winning if they don't have the key.
                    print("You couldn't get it open...")
                    Location = 0
                    sleep(1)
            elif Action.lower() == "n":
                print("You gave up on opening the door for now...")
                Location = 0
                sleep(1)
