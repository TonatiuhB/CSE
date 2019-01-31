world_map = {
    'R19A': {
        'NAME': "CLASS",
        'DESCRIPTION': "This is the class where you are at right now. two exits at the north side",
        'PATHS': {
            'NORTH': "PARKING_LOT"

        }
    },
    "PARKING_LOT": {
        'NAME': "the edison parking lot",
        'DESCRIPTION': "there are parks here. To the south is class",
        'PATHS': {
            'SOUTH': "R19A"
        }
    }
}

# vaariabsbsb

current_node = world_map ['R19A']
directions = ["NORTH,", "SOUTH," "EAST", "WEST", "UP", "DOWN"]
playing = True

# control

while playing:
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        room_name = current_node['PATHS'][command.upper()]