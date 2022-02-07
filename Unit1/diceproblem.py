import random


def dice_roll():
    return [random.randrange(1, 7) for j in range(10)]


def evaluate(x):
    return all([any([y == k for y in x]) for k in range(1, 7)])


N = 10000000
data = [evaluate(dice_roll()) for z in range(N)]
print(sum(data)/N)