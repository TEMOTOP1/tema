import random


class student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True


    def to_study(self):
        print("time to study")
        self.progress +=0.12
        self.gladness -=3

    def to_sleep(self):
        print("time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("rest time")
        self.gladness +=5
        self.progress -=1

    def is_alive(self):
        if self.progress <-0.5:
            print("new streamer")
            self.alive = False
        elif self.gladness <=0:
                print("depresenge")
                self.alive = False
        elif self.progress >5:
                print("molodec")
                self.alive = False

    def end_of_dey(self):
        print(f"Gladness = {self.gladness}")
        print(f"Gladness = {self.progress}")

    def life(self, day):
        day = f"Day {day} of {self.name} life"
        print(f"{day:=^30}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_chill()
        elif live_cube == 3:
            self.to_sleep()
        self.end_of_dey()
        self.is_alive()


vasya = student(name="Vasilyi")

for day in range(365):
    if vasya.alive == False:
        break
    vasya.life(day)

