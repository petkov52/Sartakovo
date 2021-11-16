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
        if self.food >10:
            print('{} поел'.format(name))
            self.fullness +=10
            self.food -=10
        else:
            print('У {} нет еды'.format(name))
    def work(self):
        print('{} идет на работу'.format(self.name))
        self.money +=50
        self.fullness -=10

man = Man(name='Вася')
print(name)
man.eat()
print(man)
man.work()
print(man)
