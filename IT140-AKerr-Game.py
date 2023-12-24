# Amanda Kerr
# IT-140
# Project 2

# Time module to allow for delayed text
import time

# Establish variables
inventory = []
delay = 0.75
sent_break = '-' * 30
choice = ''
current_room = ''


# Main function
def main():

    # Establish dict of room
    rooms = {
        'Vestibule': {'North': 'Greenhouse', 'South': 'Canteen', 'East': 'Rec Room', 'West': 'Airlock'},
        'Airlock': {'East': 'Vestibule', 'Item': 'Can of Spray Paint'},
        'Greenhouse': {'South': 'Vestibule', 'East': 'Lab', 'Item': 'Hose'},
        'Lab': {'West': 'Greenhouse', 'Item': 'Tube of Dangerous Chemicals'},
        'Rec Room': {'North': 'Quarters', 'West': 'Vestibule', 'Item': 'Foam Dart Blaster'},
        'Quarters': {'South': 'Rec Room', 'Item': 'pair of Safety Goggles'},
        'Canteen': {'North': 'Vestibule', 'East': 'Kitchen', 'Item': 'Tall Glass Cup'},
        'Kitchen': {'West': 'Canteen', 'Item': 'Alien Monster'}
    }

    # Function for user input
    def chz():
        global choice
        choice = input('> ')
        choice = choice.capitalize() # Allows for varied capitalization
        print(sent_break) # Keeps output screen
        print()

    # Introduction
    def intro():
        intro_txt = ['Welcome to the Io Terrabase Alpha. ',
                     'You arrived 12 days ago with your team. ',
                     'Your goal was to establish this terrabase and begin research on the moon\'s precious metals. ',
                     'However... ',
                     'while your team worked tirelessly towards your scientific goals, '
                     'your base had been unknowingly infiltrated. ',
                     'One by one your team members have vanished without a trace. ',
                     'You now know why. ',
                     'The culprit is some alien entity, '
                     'unnoticed by every probe and satellite that arrived before you. ',
                     'You are the last of your crew and '
                     'you have been working towards a plan to defeat this monstrosity. ',
                     'You must obtain 6 key items to build your alien destroying weapon. ',
                     'And you must do so before you\'re the next victim. ',
                     'If the alien finds you, it will eat you. ',
                     'Navigate the base with the following commands: ',
                     'To move room to room say: \'North\', \'South\', \'East\', or \'West\'. ',
                     'To grab an item, say: \'Grab\'.',
                     'To check your inventory, say: \'Check\'. ',
                     'If you need help knowing where to go, say: \'Help\'. ',
                     'If you would like to go over the instructions again, say \'Teach\'. ',
                     'If you would like to end your adventure, say \'Exit\'.',
                     'Now, let\'s get going before it\'s too late!'
                     ]
        for i in intro_txt: # Loop to read text to player
            print(i)
            time.sleep(delay)
        print(sent_break)
        time.sleep(delay)
        print()

    # Function to call instructions
    def teach():
        teach_txt = ['Instructions:',
                     'Your objective is to move between rooms and collect '
                     'the items you need to build your alien destroying machine.',
                     'To move to another room, you must type out a direction at the prompt.',
                     'Prompts are displayed as \'>\'.',
                     'Choices may be North, South, East, or West.',
                     'Capitalization does not matter.',
                     'Available directions can be displayed by typing \'Help\' at the prompt.',
                     'You can check your inventory by typing \'Check\'.',
                     'To exit the game, type \'Exit\'.',
                     'To repeat these instructions, type \'Teach\'.',
                     'Remember, if the alien finds you, you\'ll become its next tasty snack.'
                     ]
        for t in teach_txt: # Loop to read text to player
            print(t)
            time.sleep(delay)
        print(sent_break)
        time.sleep(delay)
        print()

    # Function for help
    def help():
        move = [key for key in rooms[current_room]] # Gets available directions (keys in current dictionary)
        print(f'You are currently in the {current_room}.')
        time.sleep(delay)
        print(f'Directions you can move: {move}')
        time.sleep(delay)
        if 'Item' in rooms[current_room]: # Shows if item in room and allows for obtaining item
            print('There is still a {} in this room. You can grab it by saying \'Grab\'.'.format(
                rooms[current_room].get('Item', 'default')))
            time.sleep(delay)
        print(sent_break)

    # Function to check inventory
    def check():
        print(f'You have collected: {inventory}') # Shows player inventory list
        time.sleep(delay)
        print(sent_break)

    # Function for adding item to inventory
    def itemgrab():
        inventory.append(rooms[current_room].get('Item', 'default')) # Adds item to inventory list
        rooms[current_room].pop('Item', 'default') # Removes item from dictionary, player cannot obtain duplicates
        print(f'You have added the {inventory[-1]} to your inventory!') # Shows most recent item added to inventory
        inventory.sort() # Sorts inventory for professional look
        time.sleep(delay)

    # Function to replay
    def replay():
        print('Would you like to play again? '
              '\nSay \'Yes\' to play again, say \'No\' to end.')
        play = input('>')
        play = play.capitalize()
        print(sent_break)
        if play == 'Yes':
            print()
            time.sleep(delay)
            main() # Runs main function again
        elif play == 'No':
            print()
            time.sleep(delay)
            print('Thank you for playing. Goodbye.')
            time.sleep(delay)
            quit() # Quits
        else:
            print('That is not an option.')
            time.sleep(delay)
            replay() # User entered non-options, repeats question

    # Function to begin
    def begin():
        global current_room
        global choice
        global inventory
        current_room = 'Vestibule' # Setting variables in this function allows for fresh replay
        choice = ''
        inventory = []
        print(f'You have been hiding out in the {current_room}. You\'re ready to get moving.'
              f'\nWhat would you like to do?')
        chz()

    # Function for loss condition met
    def end():
        end_txt = ['A delicious aroma hits your nostrils as you enter the Kitchen. ',
                   'You\'re confused. ',
                   'No one is left, so who could be cooking? ',
                   'The realization hits you just as the slimy tentacle does! ',
                   'The alien has captured you just in time for his next meal...'
                   ]
        for e in end_txt: # Loop reads text to player
            print(e)
            time.sleep(delay)
        print()
        print(sent_break)
        print('G A M E  O V E R')
        print(sent_break)
        print()
        time.sleep(delay)

    # Function for win condition met
    def win():
        win_txt = ['You stop and realize...',
                   'Finally.',
                   'You have collected all 6 items! You have everything you need!',
                   'In a matter of minutes, you build your machine.',
                   'Now is the time!',
                   'You gather your courage and venture forth to fine the alien.',
                   'You\'re off to avenge your crew...'
                   ]
        print()
        for w in win_txt: # Loop reads text to player
            print(w)
            time.sleep(delay)
        print()
        print(sent_break)
        print('C O N G R A T U L A T I O N S')
        print('You have won the game!')
        print(sent_break)
        print()
        time.sleep(delay)

    # Function loop for room movement
    def movement():
        global choice
        global current_room

        # Establish loop
        while len(inventory) < 6: # Loop for gameplay, while stops when player reaches 6 items found

            # Establish loss, replay
            if current_room == 'Kitchen':
                end() # Calls game over function
                replay() # Calls replay function

            # Exit
            elif choice == 'Exit': # Player can choose to exit when desired
                print()
                print('Thank you for playing. Goodbye.')
                time.sleep(delay)
                quit()

            # Instructions
            elif choice == 'Teach': # Allows player to repeat instructions if necessary
                teach()
                time.sleep(delay)
                print()
                print('What would you like to do?')
                chz()

            # Help
            elif choice == 'Help': # Allows player to see what directions are available to them
                help()
                time.sleep(delay)
                print()
                print('What would you like to do?')
                chz()

            # Check
            elif choice == 'Check': # Allows player to check their inventory on demand
                check()
                time.sleep(delay)
                print()
                print('What would you like to do?')
                chz()

            # Grab item
            elif choice == 'Grab':
                if 'Item' in rooms[current_room]: # Grabs item specific to current room
                    itemgrab()
                    if len(inventory) < 6: # Continues loop if player still does not have all 6 items
                        print('What would you like to do?')
                        chz()
                else: # Catches if player uses grab command with no item in room
                    print('What are you grabbing at? There\'s no items here! Try something else.')
                    chz()

            # Change current room
            elif choice in rooms[current_room] and choice != 'Item': # Calls out word item incase user types
                current_room = rooms[current_room][choice]
                if current_room == 'Kitchen': # Kitchen room ends game
                    continue
                elif 'Item' in rooms[current_room]: #text for item in room
                    print('You find yourself in the {}. You see a {} for you to grab.'
                          '\nWhat would you like to do'
                          '?'.format(current_room, rooms[current_room].get('Item', 'default')))
                    chz()
                else:
                    print(f'You are now in the {current_room}.\nWhat would you like to do?') # Text for item not in room
                    chz()

            # Invalid, other input
            else: # Catchall for any invalid entries not caught by other if/else
                print('The laws of physics don\'t allow you to do that.'
                      '\nChoose a different direction, \'Help\', \'Teach\', \'Check\', or \'Exit\', or \'Grab\' '
                      'if an item is available.')
                chz()

        # Establish win condition
        if len(inventory) == 6:
            win()
            replay()

    # Calls appropriate functions to
    intro()
    begin()
    movement()


main()
