import random
car_res = 0
doors = 3
epoch = 10000
def spoil(doors, car, res):
    spoiler = []
    for i in range(doors):
        if i != car and i != res:
            spoiler.append(i)
    if len(spoiler) == doors-1:
        exception = random.choice(spoiler)
        spoiler.remove(exception)
    elif len(spoiler) == doors-2:
        exception = car
    return spoiler, exception

for z in range(epoch):
    car = random.randint(0,doors-1)
    print("Car is at {}".format(car))
    res = random.randint(0,doors-1)
    print("You choose door {}".format(res))
    spoiler, exception = spoil(doors, car, res)
    print("A goat is found in position {}".format(spoiler))
    res = exception
    if res == car:
        print('You got the car!!!\n')
        car_res += 1
    else:
        print('You got a goat!!!\n')

print("The average prob to get a car: {}%".format(car_res/epoch*100))
