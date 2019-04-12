class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description="", items=[], characters=[]):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.items = items
        self.character = characters


class Item(object):
    def __init__(self, name, material):
        self.name = name
        self.material = material


# 0
class Sword(Item):
    def __init__(self, name, material, damage, duration=5, spawn_projectile=False):
        super(Sword, self).__init__(name, material)
        self.damage = damage
        self.swing_duration = duration
        self.spawn_projectile = spawn_projectile


# 1
class HealingConsumable(Item):
    def __init__(self, name, material, capacity=30, duration=4, cool_down=True):
        super(HealingConsumable, self).__init__(name, material)
        self.capacity = capacity
        self.consumable = True
        self.heal_over_time = duration
        self.cool_down = cool_down


# 2
class ThrowingConsumable(Item):
    def __init__(self, name, material, capacity=30, damage=10, distance=23):
        super(ThrowingConsumable, self).__init__(name, material)
        self.capacity = capacity
        self.consumable = True
        self.damage = damage
        self.throwing_distance = distance


# 3
class Axe(Item):
    def __init__(self, name, material, damage, duration=5, multi_hit=False):
        super(Axe, self).__init__(name, material)
        self.damage = damage
        self.swing_duration = duration
        self.multi_hit = multi_hit


# 4
class Staff(Item):
    def __init__(self, name, material, damage, projectile="", piercing=True):
        super(Staff, self).__init__(name, material)
        self.damage = damage
        self.projectile = projectile
        self.piercing = piercing


# 5
class Shovel(Item):
    def __init__(self, name, material, damage, duration=5, efficiency=10):
        super(Shovel, self).__init__(name, material)
        self.damage = damage
        self.swing_duration = duration
        self.efficient = efficiency


# 6
class Knife(Item):
    def __init__(self, name, material, damage, duration=2,):
        super(Knife, self).__init__(name, material)
        self.damage = damage
        self.swing_duration = duration


# 7
class WaterGun(Item):
    def __init__(self, name, material, capacity, distance=30, ):
        super(WaterGun, self).__init__(name, material)
        self.capacity = capacity
        self.range = distance
        self.trigger = True
        self.duration_of_pressure = 5


# 8
class Helmet(Item):
    def __init__(self, name, material, defense=20, enchanted=False):
        super(Helmet, self).__init__(name, material)
        self.defense = defense
        self. enchanted = enchanted


# 9
class ChestPlate(Item):
    def __init__(self, name, material, defense=50, enchanted=False):
        super(ChestPlate, self).__init__(name, material)
        self.defense = defense
        self. enchanted = enchanted


# 10
class Leggings(Item):
    def __init__(self, name, material, defense=30, enchanted=False):
        super(Leggings, self).__init__(name, material)
        self.defense = defense
        self. enchanted = enchanted


# 11
class Boots(Item):
    def __init__(self, name, material, defense=20, enchanted=False):
        super(Boots, self).__init__(name, material)
        self.defense = defense
        self. enchanted = enchanted


# 12
class Shields(Item):
    def __init__(self, name, material, defense=20, enchanted=False):
        super(Shields, self).__init__(name, material)
        self.defense = defense
        self.enchanted = enchanted


# 13
class Birb(Item):
    def __init__(self, name, material, damage=9999999999999999999999999999999999, enchanted=False, multi_hit=True,
                 healing=30, chirp=0.5):
        super(Birb, self).__init__(name, material)
        self.name = name
        self.damage = damage
        self. enchanted = enchanted
        self.multi_hit = multi_hit
        self.self_heal = healing
        self.duration = chirp


# 14
class Cannon(Item):
    def __init__(self, name, material, damage=20, reload=10):
        super(Cannon, self).__init__(name, material)
        self.damage = damage
        self.reload_time = reload


class Player(object):
    def __init__(self, starting_location):
        self.health = 10
        self.current_location = starting_location
        self.inventory = []
        self.dmg = 10

    def move(self, new_location):
        """

        :param new_location:
        :return:
        """
        self.current_location = new_location

    def print_inventory(self):
        for item in self.inventory:
            print(item.name)


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %d Health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


# items
CD = Sword("Cactus Sword", "prickly cactus", 3, 1, True)
CS = Sword("Claymore Sword", "clay", 9, 4, True)
HP = HealingConsumable("Healing Potion", "souls of degenerates", 20, 10, True)
GS = ThrowingConsumable("Grenade shot", "explosive material", 15, 55, 12)
GA = Axe("Golden Axe", "Gold", 20, 7, True)
FS = Staff("Fire staff", "i donnu", 20, "Fireball", False)
SSH = Shovel("Stone shovel", "Stone", 6, 8, 4)
PK = Knife("plastic knife", "weak plastic", 3, 1)
SG = WaterGun("SOda gun", "soda", 1, 2,)
JH = Helmet("Junk Helm", "scrap", 10, False)
JC = ChestPlate("Junk Plate", "scrap", 25, False)
JL = Leggings("Junk Leggings", "scrap", 10, False)
JB = Boots("Junk boots", "scrap", 10, False)
SS = Shields("Scrap Shield", "scrap", 45, True)
LB = Birb("Lil_birdie", "magical substance", 9999999999999999999999999999999999, True, True, 30, 0.5)
PC = Cannon("Pirate cannon", "metal i guess", 90, 50)


# characters
c1 = Character("you", 10, SSH, None)
c2 = Character("big boy", 100, CS, None)
c3 = Character("Little birdie", 90909090909090909090, LB, None)
c4 = Character("Diseased experiment", 45, CS, None)
c5 = Character("biomass", 0.5, CS, None)


# i #
A1 = Room("A1", None, "A2", None, None, " NOTE: still in a work in progress and please pick up the birb when you"
                                        " see it.: WhOa! holy crap! you seem to be in a hollow room the last thing you "
                                        "remember was the fbi throwing you in some facility. according to a "
                                        "sign on the wall it says: Room A1, Duh!"
                                        " you can go south")

A2 = Room("A2", "A1", "A3", None, None, "Room A2. you hear distant screams. its best to move on. yu can go"
                                        "south")

A3 = Room("A3", None, None, "A4", "A5", "The door behind you suddenly closes. "
                                        "You see a bird on a nearby table."
                                        " You see two doors. One to the east and one "
                                        "to the west. which will you choose", [LB], [])

A4 = Room("A4", None, None, "A3", "A6", "The door shuts behind you. To your surprise, bloody corpses"
                                        " litter the room.")
A6 = Room("A6", "A7", None, None, None, "This room has no dead bodies. There is a table in the middle of the room"
                                        "with a bowl of seeds on it. the bird happily chows down but refuses to leave"
                                        " you can go north")
A7 = Room("A7", None, None, None, None, "The room is Dark. You feel an evil presence watching you."
                                        "SNAP! you died lmao")
# rd
A5 = Room("A5", None, "A8", None, "A9", "the door suddenly shuts behind you. you see a shadow approach you"
                                        "The shadow is revealed to be an abomination of human beings meshed together"
                                        "Their screams and moans makes you cringe because no one likes them"
                                        "the birb makes quick work of it. it seems satisfied with its kill")

A8 = Room("A8", None, None, None, None, "Oh whats this? cheap death because why not bye bye")
A9 = Room("A9", None, None, None, "A10", "you see a sign that says: You're Halfway There!"                                                          
                                         "to the west is Room A10")
A10 = Room("A10", None, None, None, "A11", "THis room seems to be empty. You can go west")
A11 = Room("A11", None, None, None, "A12", "Another empty room. you slap yourself confusion. you can go west")
A12 = Room("A12", None, None, None, "A13", "Oh boy another empty room- oh look there's a camera man in the corner"
                                           "you can go west")
A13 = Room("A13", None, None, None, "A14", "A bloody mass of flesh suddenly grabs you. the bird cuts you free and you"
                                           "dash to the only door to the west as you hear a loud screech"
                                           "you can go west")
A14 = Room("A14", None, None, None, "A15", "another empty room. you and the bird run"
                                           "you can go west")
A15 = Room("A15", None, None, None, None, "The Door! you and the bird escape this weird place and end up in burger "
                                          "king")
print("░░░░░░░░░░░░░░░░▄▄▄███████▄▄░░░░░░░░░░░░")
print("░░░░░░░░░░░░░░▄███████████████▄░░░░░░░░░")
print("░░░░░░░░░░░░░█▀▀▀▄░░░░█████▀▀███▄░░░░░░░")
print("░░░░░░░░░░░░█░░▄░░█▄▄█░░░░▀▄▄█████░░░░░░")
print("░░░░░░░░░▄▀▀▀▄▄▀▀▀▀▀▀▄░░▀░░█▀▀▀░▀██░░░░░")
print("░░░░░░░▄▀░░░░░█░░░░░░▀▄▄▄▄█░░░░░░░▀▄░░░░")
print("░░░░░░▄▀░░░░░▄█▀▄▄▄▄░░░░░▄░░░░░░░░░█░░░░")
print("░░░░░░█░░░░░▄█▀▄▄▄▄▄▄▄▄▄▀▀░░░░░░░░░▀▄░░░")
print("░░░░░█░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░█░░░")
print("░░░░░█░░░░░░░░▀▄░░░░░░░░░░░░░░░░░░░░█░░░")
print("░░░░░█░░░░░░░░▄█░░░░░░░░░░░░░░░░░░░░█░░░")
print("░░░░░█░░░░░░▄▀░░░░░░░░▀▄░░░░░░░░░░░░█░░░")
print("░░░░░█░░░░░░▀▄░░░▄░░░░░█░░░░░░░░░░░░█░░░")
print("░░░░░█░░░░░░░░▀▀▀▀▀█▄▄▀░░░░░░░░░░░░░█░░░")
print("░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄██░░")
print("░░░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄▀▀▄▀▄▄")
print("░░░░▄█▀▄░░░░░░░░░░░░░░░░░░░░░░▄▄▀░░▄▀░░░")
print("░▄░▀░░█░▀▄▄░░░░░░░░░░░░░░░▄▄▄▀░░░▄▀░░░░░")
print("▀░░░░░░▀▄░░▀▄░░░░░░░░▄▄▄▀▀░░░░▄▀▀░░░░░░░")
#
player = Player(A1)


directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
playing = True

#

# control
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    if len(player.current_location.items) > 0:
        pickup = input("hey! there's something here. pick it up?")
        if pickup == "yes":
            print("you picked the item. move now.")
            print("this is what you have:")
            player.inventory = player.inventory + player.current_location.items
            player.print_inventory()
        if pickup == "no":
            print("you refuse to pick up the item. move on")
    command = input(">_")
    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            room_name = getattr(player.current_location, command)
            room_object = globals()[room_name]

            player.move(room_object)
        except KeyError:
            print("this key no exist")

    else:
        print("command not recognized")