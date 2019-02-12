world_map = {
    'ROOM1': {
        'NAME': "NEST",
        'DESCRIPTION': "look, its your nest. You are well rested now, but you must stop the cannibal."
        "Find cannibal tokens to strengthen your power",
        'PATHS': {
            'NORTH': "ROOM4",
            'SOUTH': "ROOM2",


        }
    },
    'ROOM4': {
        'NAME': "ELDER TREE N",
        'DESCRIPTION': "One of the elder tress. There seems to be nothing here.You can go south or east",
        'PATHS': {
            'SOUTH': "NEST"
        }
    },
    'ROOM2': {
        'NAME': "ELDER TREE S",
        'DESCRIPTION': "One of the elder tress. You hear distressed chirping"
        "You hear the cannibal's roar in the distance",
        'PATHS': {
            'SOUTH': "NEST"
        }
    }
},

# vaariabsbsb

current_node = world_map ['R19A']
directions = ["NORTH,", "SOUTH," "EAST", "WEST", "UP", "DOWN"]
playing = True

# control

while playing:
    print(current_node['NAME'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("hey dumb dumb you cant go there")

    else:
        print("command not recognixed")
