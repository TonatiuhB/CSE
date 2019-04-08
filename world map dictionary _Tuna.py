world_map = {
    'ROOM1': {
        'NAME': "NEST",
        'DESCRIPTION': "look, its your nest. You are well rested now, but you must stop the cannibal."
        "Find cannibal tokens to strengthen your power. you can go north or south",
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
    'ROOM5': {
        'NAME': "R5",
        'DESCRIPTION': "You suddenly fall across the room and die. good job",
        'PATHS': {

        }
    },
    'ROOM2': {
        'NAME': "ELDER TREE S",
        'DESCRIPTION': "One of the elder tress. You hear distressed chirping"
                "You hear the cannibal's roar in the distance",
        'PATHS': {
            'NORTH': "NEST",
            'SOUTH': "ROOM6",
        }
    },
    'ROOM6': {
        'NAME': "R6",
        'DESCRIPTION': "This is R6. seems to be nothing here but a pile of seeds . you can go south",
        'PATHS': {
            'NORTH': "ROOM2",
            'SOUTH': "ROOM6",
        }
    },
    'ROOM7': {
        'NAME': "R7",
        'DESCRIPTION': "This is R7. you found a token! Good job!. you can go south",
        'PATHS': {
            'SOUTH': "ROOM8",
            'NORTH': "ROOM6"
        }
    },
    'ROOM8': {
        'NAME': "R8",
        'DESCRIPTION': "Entering the room causes the door you came from lock down. you can go west",
        'PATHS': {
            'WEST': "ROOM9"
        }
    },
    'ROOM9': {
        'NAME': "R9",
        'DESCRIPTION': "This room has a bird!. it chirps nervously. you think the bird is trying to warn you.",
        'PATHS': {
            'WEST': "ROOM10"
        }
    },
    'ROOM10': {
        'NAME': "R10",
        'DESCRIPTION': "a room with a table and a cannibal token! You can go west",
        'PATHS': {
            'WEST': "ROOM11"
        }
    },
    'ROOM 11': {
        'NAME': "R10",
        'DESCRIPTION': "this room is covered in fleshy biomass. you can go west",
        'PATHS': {
            'WEST': "ROOM12"
        }
    },
    'ROOM 12': {
        'NAME': "R10",
        'DESCRIPTION': "this room is covered in fleshy biomass. you can go west",
        'PATHS': {
            'WEST': "ROOM13"
        }
    },
    'ROOM 13': {
        'NAME': "R10",
        'DESCRIPTION': "this room is covered in fleshy biomass. you can go west",
        'PATHS': {
            'WEST': "ROOM14"
        }
    },
    'ROOM 14': {
        'NAME': "R10",
        'DESCRIPTION': "this room is also covered in fleshy biomass. you can go west",
        'PATHS': {
            'WEST': "ROOM15"
        }
    },
    'ROOM 15': {
        'NAME': "R10",
        'DESCRIPTION': "THE CANNIBAL!. Using the cannibal tokens you consume the cannibal and you become one. good job",
        'PATHS': {
            'WEST': "ROOM15"
        }
    },

}

# vaariabsbsb

current_node = world_map["ROOM1"]
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True

# control
while playing:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
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
