def gcd(x,y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if x % i == 0 and y % i == 0:
            gc = i
    return gc


print(gcd(60,48))


def lcm(x,y):
    if x > y:
        grt = x
    else:
        grt = y
    while True:
        if grt % x == 0 and grt % y == 0:
            lcm=grt
            break
        grt += 1
    return lcm


print(lcm(12,20))