#!/usr/bin/python3
"""This Program was created by Blake Ellsworth with some borrowed code from Alta3 Lab 68. Github DTNevaeha"""


from pydoc import describe
stepCounter = 0


def gameStart():
    """These are the game instructions that show when you hit play"""

    # print a main menu and the commands
    print('''
   
   You are an expendable side character named Pete.
   You are in an action film, but you really want to survive.
   You didnt bother reading the script and have no idea who the main character is.

   You must search around and make decisions to figure out who is the main character.
   Make wrong choices and you'll die like the expendable character you are.
   
   This game is still in progress and nowhere near complete. Please take considerations
    
    Welcome to Side-Quest: Prepare to Die Edition
    
    ========
    Commands:
      go [direction]
      get [item]
      inspect [name]
    ''')


def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print(room[currentRoom]['description'])
    print(f'You have taken {stepCounter} steps')

    # print what the player is carrying
    print('Inventory:', inventory)
    # print('\n')
    # check if there's an item in the room, if so print it
    if "item" in room[currentRoom]:
        print('You can get a ' + room[currentRoom]['item'])
    if "inspect" in room[currentRoom]:
        print('You can inspect the ' + room[currentRoom]['inspect'])
    if "people" in room[currentRoom]:
        print(room[currentRoom]['people'] + ' is in this room')
        print("---------------------------")


# This shows your inventory
inventory = []

# List of possible rooms, items, and inspectables
room = {

    # This is the library with directions, inspectables, people, and description
    'Library': {
        'south': 'Sun Room',
        'east': 'Hall',
        'west': 'Secret',
        'item': 'donut',
        'inspect': 'table',
        'people': 'Gerald' + " and " + 'tony',
        'description': 'You can go south or east \n You hear nothing to the East \n You hear loud scratching noises to the South \n'

    },
    # This is the Sun Room with directions, inspectables, and description
    'Sun Room': {
        'north': 'Library',
        'east': 'Garden',
        'inspect': 'dog',
        'item': 'fuel canister',
        'description': 'You can go north or east \n You hear the sound of someone shouting in the loudest whisper you ever heard to the north \n You see someone digging a deep hole to the East \n'
    },

    # This is the Hall with directions, items, and description
    'Hall': {
        'west': 'Library',
        'south': 'Garden',
        'north': 'Dining Room',
        'east': 'Bed Room',
        'item': 'potion',
        'description': 'You can go North, South, East, West \n To the west you hear the sound of pages flipping \n Sounds of digging come from the south \n Loud chattering comes from the north \n An eerie silence to the east \n'
    },

    # This is the Garden with directions and description
    'Garden': {
        'north': 'Hall',
        'west': 'Sun Room',
        'south': 'Landing Pad',
        'east': 'Forest',
        'description': 'You can go North, South, East, West \n You hear nothing to the North \n You hear barking to the West \n A loud engine sound comes from the south \n Chanting and howling comes from the East \n'
    },

    # This is the landing Pad with directions, inspectables and description
    'Landing Pad': {
        'north': 'Garden',
        'inspect': 'Helicopter',
        'description': 'You can go north \n You realize you have made a mistake and this is not the main character \n'
    },

    # This is the Forest with directions and description
    'Forest': {
        'west': 'Garden',
        'east': 'Stream',
        'description': 'You can go west or east \n Sounds of digging come from the West \n Sounds of a raging river come from the east \n'
    },

    # This is the Stream with directions and description
    'Stream': {
        'west': 'Forest',
        'description': 'You can go west \n You hear a whisper on the wind, flying is dangerous! \n'
    },

    # This is the Bed Room with directions and description
    'Bed Room': {
        'west': 'Hall',
        'description': 'You can go West \n You hear the sound of someone walking passed \n'
    },

    # This is the Dining Room with directions and description
    'Dining Room': {
        'south': 'Hall',
        'north': 'Kitchen',
        'description': 'You can go North or South \n You hear the sounds of cooking and clatter to the north \n You look to the south are still trying to find the bathroom \n'
    },

    # This is the Kitchen with directions and description
    'Kitchen': {
        'south': 'Dining Room',
        'description': 'You can go south \n You overhear someone talking about a secret bookshelf \n'
    },

    'Secret': {
        'east': 'Library',
        'item': 'script',
        'description': 'You can go East \n You are wondering who allowed someone to bring a donut into the library \n'
    }
}

# start the player in the Hall
currentRoom = 'Library'

gameStart()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in room[currentRoom]:
            # set the current room to the new room
            currentRoom = room[currentRoom][move[1]]
            stepCounter += 1
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in room[currentRoom] and move[1] in room[currentRoom]['item']:
            # add the item to their inventory
            inventory.append(move[1])
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item key:value pair from the room's dictionary
            del room[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    if move[0] == 'inspect':
        # Makes sure there is something inspectable in the room
        if "inspect" in room[currentRoom]:
            print(move[1] + ' - You inspected the item!')

    # If a player enters a room with a dog and a donut then they die
    if 'inspect' in room[currentRoom] and 'dog' in room[currentRoom]['inspect'] and 'donut' in inventory:
        print('You see a friendly Doberman, you reach out to pet it \n The Doberman smells your donut and attacks you \n YOU DIED! \n The doberman is not the main characte')
        break

        # If a player enters the forest with fuel then they die
    if 'inspect' in room[currentRoom] and 'dog' in room[currentRoom]['inspect'] and 'donut' in inventory:
        print('You see a friendly Doberman, you reach out to pet it \n The Doberman smells your donut and attacks you \n YOU DIED! \n The doberman is not the main character, just hungry')
        break


# Define how a player can win
    if currentRoom == 'Secret' and 'donut' in inventory and 'script' in inventory:
        print('You finally stopped to eat your donut and read the script and just realized... YOU are the main character \n You WIN!')
        break
