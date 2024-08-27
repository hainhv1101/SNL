import random

squares = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100,
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78,
}
squares2 = {
    2: 23, 6: 45, 20: 59, 43: 17, 50: 5, 52: 72, 56: 8, 57: 96, 71: 92,
    73: 15, 84: 63, 87: 49, 98: 40
}
print(f'{"Rolls":^20}{"Average Rolls":^20}')
totalrolls = 0
for i in range(100000):
    rolls = 0
    curr = 1
    while curr != 100:
        thisMove = random.randint(1, 6)
        curr += thisMove
        rolls += 1
        if curr > 100:
            curr = 100 - (curr - 100)
        if curr in squares2:
            curr = squares2[curr]
    totalrolls += rolls
    print(f'{rolls =:^20}{totalrolls / (i + 1)}')
