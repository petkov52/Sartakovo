class Animal():
    def __init__(self):
        self.legs = 2
        self.name = 'Dog'
        self.color= 'Spotted'
        self.smell= 'Alot'
        self.age  = 10
        self.kids = 0

an = Animal()
attrs = vars(an)
# {'kids': 0, 'name': 'Dog', 'color': 'Spotted', 'age': 10, 'legs': 2, 'smell': 'Alot'}
# now dump this in some way or another
# print(', '.join("%s: %s" % item for item in attrs.items()))

print(item for item in attrs.items())