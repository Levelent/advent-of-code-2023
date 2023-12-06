import math

times = [int(num) for num in input().split()[1:]]
dists = [int(num) for num in input().split()[1:]]

total = 1
for time, dist in zip(times, dists):

    # Use the quadratic formula, with a=1, b=-time, c=dist
    discriminant = math.sqrt(time * time - 4 * dist)

    # as we are looking for < 0 and not <= 0, need to round correctly
    upper = math.ceil((time + discriminant) / 2 - 1)
    lower = math.floor((time - discriminant) / 2 + 1)

    total *= upper - lower + 1

print(total)