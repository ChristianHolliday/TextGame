# Christian Holliday
# Game start message
def game_start():
    print('|' + ('-' * 72) + '|')
    print('|' + ' ' * 17 + 'Welcome to Shadows of the Necromancer!' + ' ' * 17 + '|')
    print('|' + (' ' * 72) + '|')
    print('|Commands: go South, go North, go East, go West, Exit, Search, Inventory |')
    print('|' + (' ' * 72) + '|')
    print(('|' + ' ' * 11) + 'Collect all items before fighting the Necromancer!' + (' ' * 11 + '|'))
    print('|' + (' ' * 72) + '|')
    print('|' + ('-' * 72) + '|')


# Search room for item and let player know if/what item found
def search_room(room):
    if 'items' in rooms[room]:
        items = rooms[room]['items']
        print(f"You found: {', '.join(items)}")
        return items
    else:
        print("No items to search in this room.")
        return []


def boss_fight():
    border_width = 87
    message = [
        "You have entered the Throne Room, the lair of the Necromancer!",
        "The air is thick with dark magic and a menacing presence fills the chamber.",
        "The Necromancer stands before you, his eyes glowing with malevolent power.",
        "Prepare yourself for the final confrontation!",
        "With the ancient items you have gathered, you have the strength to face him. Good luck!",
        "",
        "After a fierce battle, you emerge victorious!",
        "Congratulations! You have defeated the Necromancer and saved the land!",
        "The darkness has been vanquished and peace is restored.",
        "You are hailed as a hero. Your quest is complete.",
        "Thank you for playing!"
    ]
    # Print bordered message for boss fight and center lines
    print('*' * (border_width + 4))
    for line in message:
        print('* ' + line.center(border_width) + ' *')
    print('*' * (border_width + 4))


# Check if all required items have been collected and inventory has not been checked yet
def check_inventory(inventory, all_items, has_checked_inventory):
    if all_items.issubset(set(inventory)) and not has_checked_inventory:
        print('+' * 62)
        print('Congratulations! You have collected all the items.')
        print('You are ready to face the Necromancer!')
        print('Feel free to continue exploring or proceed to the Throne Room when you are ready.')
        print('+' * 62)
        has_checked_inventory = True
    return has_checked_inventory


def display_inventory(inventory):
    print()
    print('*' * 50)
    print('*' + ' ' * 19 + 'INVENTORY' + ' ' * 19 + ' *')
    print('*' * 50)

    if inventory:
        for item in inventory:
            print('* ' + item.ljust(46) + ' *')
    else:
        print('* ' + 'Your inventory is empty.'.center(46) + ' *')

    print('*' * 50)
    print()


# Room available directions and associated items
rooms = {
    'Village Square': {
        'West': 'Enchanted Forest'
    },
    'Enchanted Forest': {
        'East': 'Village Square',
        'South': 'Haunted Cemetery',
        'items': ['Ancient Sword']
    },
    'Haunted Cemetery': {
        'West': 'Cursed Swamp',
        'North': 'Enchanted Forest',
        'East': 'Laboratory',
        'South': 'Ancient Library',
        'items': ['Scroll of Light']
    },
    'Cursed Swamp': {
        'East': 'Haunted Cemetery',
        'items': ['Holy Water']
    },
    'Ancient Library': {
        'North': 'Haunted Cemetery',
        'East': 'Tower of Shadows',
        'items': ['Mystic Amulet']
    },
    'Laboratory': {
        'West': 'Haunted Cemetery',
        'South': 'Tower of Shadows',
        'North': 'Throne Room',
        'items': ['Healing Potion']
    },
    'Tower of Shadows': {
        'North': 'Laboratory',
        'West': 'Ancient Library',
        'items': ['Shadow Key']
    },
    'Throne Room': {
        'South': 'Laboratory'
    }
}


def main():
    game_start()
    print()
    print()
    # Prompt player to start game
    game_control = input('>>>> Type Start to begin!').strip()
    # Validate start command
    while game_control.lower() != 'start':
        game_control = input('>>>> Invalid command. Please type \'Start\' to begin').strip()

    # Initialize game state
    current_room = 'Village Square'
    inventory = []
    all_items = {'Ancient Sword', 'Scroll of Light', 'Holy Water', 'Mystic Amulet', 'Healing Potion', 'Shadow Key'}
    has_checked_inventory = False

    # Game loop
    while True:
        # Display available directions
        commands = [key if key != 'items' else 'Search for items' for key in rooms[current_room].keys()]
        commands.append('Inventory')  # Add Inventory to the list of commands
        commands_str = ', '.join(commands)
        print(f'Current Room: {current_room}. Available commands: {commands_str}.')
        game_control = input('>>>> Enter direction command, Search, Inventory, or Exit:').strip()

        # Handle exit command
        if game_control.lower() == 'exit':
            print()
            print('<>' * 25)
            print('The dark reign of the Necromancer spreads across the land.')
            print('Your quest to save the world has failed. The shadows have won.')
            print('Perhaps a new hero will rise to challenge the darkness...')
            print('<>' * 25)
            input("\n>>>> Press Enter to exit the game...")  # Keeps the window open
            break

        command = game_control.split()
        # Handle movement and search commands
        if len(command) == 2 and command[0].lower() == 'go':
            direction = command[1].capitalize()
            if direction in rooms[current_room]:
                next_room = rooms[current_room][direction]
                if next_room == 'Throne Room':
                    if all_items.issubset(set(inventory)):
                        if not has_checked_inventory:
                            has_checked_inventory = check_inventory(inventory, all_items, has_checked_inventory)
                        boss_fight()
                        input("\n>>>> Press Enter to exit the game...")  # Keeps the window open
                        break  # Exit the game after the boss fight
                    else:
                        # Story of what happens if player enters without all items
                        print('-' * 87)
                        print("You have entered the Throne Room, but something is terribly wrong.")
                        print("Without all of the sacred items, the dark power of the Necromancer overwhelms you.")
                        print(
                            "In a flash, your body is consumed by shadows, and your soul is trapped in eternal darkness.")
                        print("The land falls deeper into despair as the Necromancer's reign continues unchallenged.")
                        print("Your journey ends here... and so does the hope of the world.")
                        print('-' * 87)
                        input("\nPress Enter to exit the game...")  # Keeps the window open
                        break  # End the game as the player dies
                else:
                    current_room = next_room
            else:
                print('You cannot go that way.')
        elif game_control.lower() == 'search':
            items = search_room(current_room)
            if items:
                inventory.extend(items)
                # Remove items from the room
                rooms[current_room].pop('items', None)
        elif game_control.lower() == 'inventory':
            display_inventory(inventory)
        else:
            print('Invalid command. Please use "go [direction]", "Search", "Inventory", or "Exit".')

        # Check if the player has collected all items
        if all_items.issubset(set(inventory)):
            has_checked_inventory = check_inventory(inventory, all_items, has_checked_inventory)


if __name__ == "__main__":
    main()
