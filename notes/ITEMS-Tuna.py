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


DS = Sword("Diamond Sword", "Diamond", 5, 9, True)
CD = Sword("Cactus Sword", "prickly cactus", 3, 1, True)
CS = Sword("Claymore Sword", "clay", 2, 4, True)


# 1
class HealingConsumable(Item):
    def __init__(self, name, material, capacity=30, duration=4, cool_down=True):
        super(HealingConsumable, self).__init__(name, material)
        self.capacity = capacity
        self.consumable = True
        self.heal_over_time = duration
        self.cool_down = cool_down


HP = HealingConsumable("Healing Potion", "souls of degenerates", 20, 10, True)


# 2
class ThrowingConsumable(Item):
    def __init__(self, name, material, capacity=30, damage=10, distance=23):
        super(ThrowingConsumable, self).__init__(name, material)
        self.capacity = capacity
        self.consumable = True
        self.damage = damage
        self.throwing_distance = distance


PP = ThrowingConsumable("Poison Potion", "snake venom", 10, 34, 14)


# 3
class Axe(Item):
    def __init__(self, name, material, damage, duration=5, multi_hit=False):
        super(Axe, self).__init__(name, material)
        self.damage = damage
        self.swing_duration = duration
        self.multi_hit = multi_hit


SA = Axe("Stone axe", "Stone", 12, 7, True)


# 4
class Staff(Item):
    def __init__(self, name, material, damage, projectile="", piercing=True):
        super(Staff, self).__init__(name, material)
        self.damage = damage
        self.projectile = projectile
        self.piercing = piercing


FS = Staff("Fire staff", "i donnu", 20, "Fireball", False)


# 5
class Shovel(Item):
    def __init__(self, name, material, damage, duration=5, efficiency=10):
        super(Shovel, self).__init__(name, material)
        self.damage = damage
        self.swing_duration = duration
        self.efficient = efficiency


SSH = Shovel("Stone shovel", "Stone", 6, 8, 4)


# 6
class Knife(Item):
    def __init__(self, name, material, damage, duration=2,):
        super(Knife, self).__init__(name, material)
        self.damage = damage
        self.swing_duration = duration


PK = Knife("plastic knife", "weak plastic", 3, 1)


# 7
class WaterGun(Item):
    def __init__(self, name, material, capacity, distance=30, ):
        super(WaterGun, self).__init__(name, material)
        self.capacity = capacity
        self.range = distance
        self.trigger = True
        self.duration_of_pressure = 5


SG = WaterGun("SOda gun", "soda", 1, 2,)


# 8
class Helmet(Item):
    def __init__(self, name, material, defense=20, enchanted=False):
        super(Helmet, self).__init__(name, material)
        self.defense = defense
        self. enchanted = enchanted


JH = Helmet("Junk Helm", "scrap", 10, False)


# 9
class ChestPlate(Item):
    def __init__(self, name, material, defense=50, enchanted=False):
        super(ChestPlate, self).__init__(name, material)
        self.defense = defense
        self. enchanted = enchanted


JC = ChestPlate("Junk Plate", "scrap", 25, False)


# 10
class Leggings(Item):
    def __init__(self, name, material, defense=30, enchanted=False):
        super(Leggings, self).__init__(name, material)
        self.defense = defense
        self. enchanted = enchanted


JL = Leggings("Junk Leggings", "scrap", 10, False)


# 11
class Boots(Item):
    def __init__(self, name, material, defense=20, enchanted=False):
        super(Boots, self).__init__(name, material)
        self.defense = defense
        self. enchanted = enchanted


JB = Boots("Junk boots", "scrap", 10, False)


# 12
class Shields(Item):
    def __init__(self, name, material, defense=20, enchanted=False):
        super(Shields, self).__init__(name, material)
        self.defense = defense
        self. enchanted = enchanted


SS = Shields("Scrap Shield", "scrap", 45, True)


# 13
class Birb(Item):
    def __init__(self, name, material, damage=9999999999999999999999999999999999, enchanted=False, multi_hit=True,
                 healing=30, chirp=0.5):
        super(Birb, self).__init__(name, material)
        self.damage = damage
        self. enchanted = enchanted
        self.multi_hit = multi_hit
        self.self_heal = healing
        self.duration = chirp


LB = Birb("Lil_birdie", "magical substance", 9999999999999999999999999999999999, True, True, 30, 0.5)


# 14
class Cannon(Item):
    def __init__(self, name, material, damage=20, reload=10):
        super(Cannon, self).__init__(name, material)
        self.damage = damage
        self.reload_time = reload


PC = Cannon("Pirate cannon", "metal i guess", 90, 50)