from random import randint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, {} сытость '.format(self.name, self.fullness,)

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 20
            self.house.food -= 10

        else:
            print('У {} нет еды'.format(self.name))

    def work(self):
        print('{} идет на работу'.format(self.name))
        self.house.money += 50
        self.fullness -= 10

    def play_DOTA(self):
        self.fullness -= 10
        print('{} играл в доту целый день'.format(self.name))

    def go_to_shop(self):
        self.house.food += 20
        self.house.money -= 10
        print('{} cходил в магазин'.format(self.name))


    def act(self):
        if self.fullness == 0:
            self.eat()
        elif self.house.money < 10:
            self.work()
        elif self.house.food < 10:
            self.go_to_shop()
        else:
            dice = randint(1, 6)
            if dice == 1:
                self.work()
            elif dice == 2:
                self.eat()
            else:
                self.play_DOTA()

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -=10
        print('{} заехал в дом'.format(self.name))


class House:
    def __init__(self):
        self.food = 10
        self.money = 50
    def __str__(self):
        return 'В доме - {} еды, - {} денег '.format(
            self.food, self.money)





citizens = [
    Man(name= 'Бивис'),
    Man(name= 'Батхед'),
    Man(name='Кенни')

]
my_sweet_home = House()

for citizen in citizens:
    citizen.go_to_the_house(house=my_sweet_home)


bivis = Man(name='Бивис')
butthed = Man(name='Бадхед')


days = 0
for i in range(1, 100):
    print('\nXXXXXXXXXXXXXXX    {}  день  XXXXXXXXXXXXXXX\n'.format(days))
    for citizen in citizens:
        citizen.act()
    print('______________ В конце дня _____________')
    for citizen in citizens:
        print(citizen)

    print(my_sweet_home)
    days += 1
