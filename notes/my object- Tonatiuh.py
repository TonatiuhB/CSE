class PARROT(object):
        def __init__(self, chirp, distance=30, nice=5, alive=True):
            self.chirp = chirp
            self.fly = distance
            self.fluff = nice
            self.alive = alive
            self.duration_of_chirp = 134526738495876
        def shoot(self, time):
            if self.alive:
               if self.duration_of_chirp <= 0:
                    print("Your parrot has stopped chirping")
               elif self.duration_of_chirp < time:
                   print("your bird decides to stop chirping after %s seconds", self.duration_of_chirp)
                   self.duration_of_chirp = 0
               else:
                  print("your parrot suddenly chirps for %s seconds" % time)
                  self.duration_of_chirp -= time
            else:
                print("Ho ho ho ha ha, ho ho ho he ha your bird dead")
        def feed_a_berry(self):
            self.duration_of_chirp = 5
            print("you feed the parrot a berry and now he is happy")


my_parrot = PARROT(7, 40, True)
your_parrot = PARROT(3, 2, False)
gods_parrot = PARROT(213425637485906594837625435678950432987656378959584736254341567524516782930498763,
                     1324567689706598473625, True)

my_parrot.shoot(4)
my_parrot.feed_a_berry()
my_parrot.shoot(6)
your_parrot.shoot(5)
gods_parrot.shoot(213425637485906594837625435678950432987656378959584736254341567524516782930498763)