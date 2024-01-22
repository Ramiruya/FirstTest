import math
v = int(input('v:'))
a = float(input('a:'))
l = ((v**2)*math.sin(math.radians(2*a)))/9.8
print(l)

checkabc = input('Ось х статична?')
if checkabc == 'Да' or checkabc == 'да':
    for v in range(45, 51):
        for a in range(1, 91):
            x = v**2*math.sin(math.radians(2*a))/9.8
            if x<=8:
                print(v, a, x)
print('Hello world!')

gen= [5*a for a in range(1, 11)]
print(gen)