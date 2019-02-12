class WaterGun(object):
    def __init__(self, capacity, distance, stock):
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

my_water_gun = WaterGun()