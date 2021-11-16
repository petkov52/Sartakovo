from random import randint


class Man:


    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 0

    def __str__(self):
        return 'Я - {}, сытость {}, еды осталось {}, денег осталось  {}'.format(
            self.name, self.fullness, self.food, self.money)


    def eat(self):
        if self.food > 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.food -= 10
            self.money -=25
        else:
            print('У {} нет еды'.format(self.name))




    def work(self):
        print('{} идет на работу'.format(self.name))
        self.money += 50
        self.fullness -= 10

    def play_DOTA(self):
        self.fullness -= 10
        print('{} играл в доту целый день'.format(self.name))

    def act(self):
        if self.fullness <=0:
            self.eat()
        dice = randint(1, 6)
        if dice == 1:
            self.work()
        elif dice ==2:
            self.eat()
        else:
            self.play_DOTA()


man_Vasia = Man(name='Вася')
print(man_Vasia)
days = 0
for i in range(1,30):
    man_Vasia.act()
    days +=1
    print(man_Vasia)
    print(days)
