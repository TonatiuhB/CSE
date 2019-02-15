import Special_Random


class WaterGun(object):
    def __init__(self, capacity, distance=30, stock=False):
        # things that a WaterGun has
        # all of these should be relevant to our program
        self.capacity = capacity
        self.range = distance
        self.trigger = True
        self.stock = stock
        self.duration_of_pressure = 5

    def shoot(self, time):
        if self.trigger:
           if self.duration_of_pressure <= 0:
                print("there is no pressure hyuck")
           elif self.duration_of_pressure < time:
               print("you run out of pressure after firing %s seconds", self.duration_of_pressure)
               self.duration_of_pressure = 0
           else:
              print("ypu shoot for %s seconds" % time)
              self.duration_of_pressure -= time
        else:
            print("there is no trigger!")
    def pump_it_up(self):
        self.duration_of_pressure = 5
        print("you pump back to full pressure")


# Initialize the objects
my_water_gun = WaterGun(5.2, 40, True)
your_water_gun = WaterGun(1.0, 1, False)
ww_water_gun = WaterGun(9999999999, 999999999999999999, True)
yahir_water_gun = WaterGun(0.1)


# do stuff
my_water_gun.shoot(5)
my_water_gun.shoot(1)
my_water_gun.pump_it_up()
my_water_gun.shoot(2)
ww_water_gun.shoot(99999999)
print(Special_Random.Randomwiebe.special_random())