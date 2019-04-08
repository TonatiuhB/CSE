class Vehicle(object):
    def __init__(self, name, engine):
        self.name = name
        self.engine_type = engine


class Car(Vehicle):
    def __init__(self, name, engine_type, body_type):
        super(Car, self).__init__(name, engine_type)
        self.body_type = body_type
        self.steering_wheel = True
        self.engine_status = False
        self.fuel = 100

    def start_engine(self):
        self.engine_status = True
        print("you turn the car on you nimrod")

    def move_forward(self):
        self.fuel -= 1
        print("you move forward")

    def turn_left(self):
        self.fuel -= 1
        print("you move left")

    def turn_off(self):
        self.engine_status = False
        print("ur carrrrrrr off")


class Corvette(Car):
    def __init__(self):
        super(Corvette, self).__init__("Corvette", "Gas", "slim")



class KeylesCar(Car):
    def __init__(self, name, engine_type, body_type):
        super(KeylesCar, self).__init__(name, engine_type, body_type)

    def start_engine(self):
        self.engine_status = True
        print("PUSH BUTTON NOW CAR GO VROOM")



juul_car = Corvette()
juul_car.start_engine()
juul_car.move_forward()

adammmmmmmmm_car = KeylesCar("adams caro", "Diesel", "Toaster")
adammmmmmmmm_car.start_engine()
adammmmmmmmm_car.move_forward()
adammmmmmmmm_car.turn_off()
