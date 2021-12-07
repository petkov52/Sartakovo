class Bread:

    def __str__(self):
        return 'хлеб'

    def __add__(self, other):
        return Sandwich(self, other)


class Chesse:
    def __str__(self):
        return 'сыр'

    def __add__(self, other):
        return Sandwich(self, other)


class Sausage:

    def __str__(self):
        return 'колбаса'

    def __add__(self, other):
        return Sandwich(self, other)


class Sandwich:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2
        print(self.part1, part2)

    def __str__(self):
        if str(self.part1) == 'хлеб' and str(self.part2) == 'колбаса':
            return 'Я бутерброд c колбасой. Состою из ' + str(self.part1) + ' и ' + str(self.part2)
        elif str(self.part1) == 'хлеб' and str(self.part2) == 'сыр':
            return 'Я бутерброд c сыром. Состою из ' + str(self.part1) + ' и ' + str(self.part2)
        else:
            return 'Я хер знает что'

borodinsky = Bread()
borodinsky1 = Bread()
salami = Sausage()
tilzit = Chesse()

print(borodinsky + tilzit)
