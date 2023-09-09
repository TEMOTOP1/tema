import random


class Human:
    def __init__(self, name="human" , job=None, car=None, home=None  ):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = Home()

    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = job(job_list)

    def eat(self):
        if self.home.food <=0:
            self.shoping("food")
        else:
            if self.satiety >100:
                self.satiety =100
                return
        self.satiety += 5
        self.home.food -= 5

    def work(self):
        if self.car.drive():

            pass
        else:
            if self.car.fuel <20:
                self.shoping("fuel")
                return
            else:
                self.to_repair()
            return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shoping(self, manage):
        if self.car.drive():

            pass
        else:
            if self.car.fuel < 20:
                self.shoping("fuel")
                return
            else:
                self.to_repair()
        if manage == "fuel":
            print ("i bought fuel")
            self.money -=100
            self.car.fuel +=100
        elif manage == "food":
            print("i bought food")
            self.money -=50
            self.home.food +=50
        elif manage == "delicacies":
            print("delicacies!!!")
            self.gladnes += 10
            self.satiety += 2
            self.money -=15

    def chill(self):
        self.gladness +=15
        self.home.mess += 5


    def clean_home(self):
         self.gladness -=5
         self.home.mess =0

    def to_repair(self):
        self.car.strenght += 100
        self.money -=50

    def day_indexes(self, day):
        day = f"Today is {day} of {self.name}'s life"
        print(f"{day:=^50}","\n")
        human_indexes =  self.name + "'s indexes"
        print(f"{human_indexes}:^50", "\n")
        print(f"money - {self.money}")
        print(f"satiety - {self.satiety}")
        print(f"gladness - {self.gladness}")
        home_index = "home indexes"
        print(f"{home_index:^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strenght}")


    def is_alive(self):
        if self.gladness< 0:
            print("depresia")
            return False
        if self.satiety < 0:
            print("Dead")
            return False
        if self.money < -500:
            print("banckrot")
            return  False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            self.get_home()
        if self.car is None:
            self.get_car()
        if self.job is None:
            self.get_job()
        self.day_indexes(day)
        dise = random.randint(1, 4)
        if dise == 1:
            print("time to chill")
            self.chill()
        elif dise == 2:
            print("time to work")
            self.work()
        elif dise == 3:
            print("time to clean")
            self.clean_home()
        elif dise == 4:
            print("time to treats")
            self.shoping(manage="delicacies")


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strenght = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
    def drive(self):
        if self.strenght >0 and self.fuel>= self.consumption:

            self.fuel -= self.consumption
            self.strenght -= 1
            return True
        else:
            print("The car cannot move")
            return  False


class Home:
            def __init__(self):
                self.food = 0
                self.mess = 0


class job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


job_list = {
    "java dev": {"salary": 50, "gladness_less": 10},
    "phytoon dev": {"salary": 40, "gladness_less": 3},
    "C++ dev": {"salary": 45, "gladness_less": 25},
    " Rust": {"salary": 70, "gladness_less": 1}
}

brand_of_car = {
    "BMW":{"fuel": 100,  "strength": 180, "consumption": 6},
    "lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "wolwo": {"fuel": 80, "strength": 150, "consumption": 8},
    "ferari": {"fuel": 80, "strength": 120, "consumption": 14}
}

hum = Human(name="Vasya")

for day in range(1, 8):
    if hum.live(day) == False:
        break