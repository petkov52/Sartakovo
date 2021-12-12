import math

PI = math.pi


def inner_radius():
    a = float(input('Внутренний диаметр цилиндра в см: '))
    r = a / 2
    return r


def outer_radious():
    a = float(input('Внешний диаметр цилиндра в см: '))
    r = a / 2
    return r

def height():
    h = float(input('Высота цилиндра в см:  '))
    return h


def volume():
    inner_rad = inner_radius()
    outer_rad = outer_radious()

    h=height()
    inner_s = PI*inner_rad**2
    outer_s = PI*outer_rad**2
    s=outer_s-inner_s
    v= s * h
    return round(v/1000,1)



def mass(g):
    m = 0.5
    result = (round(m*g,1),g)

    return' Масса угля в кг:',result[0],'Объем цилиндра в литрах:',result[1]

#print(mass(volume()))
list = list(mass(volume()))
print(list[0], list[1],'\n',list[2], list[3])

#print('Масса угля в кг:', mass(volume()[0]),'Объем цилиндра в литрах:')
