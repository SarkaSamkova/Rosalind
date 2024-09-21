def mortal_rabbits(months, alive):
    categories = {}
    sum_list = []

    # dc: 0 - newborns, 1..3 - age in months, 4 - adults (predead)
    for i in range(alive):
        categories[i] = 0
    categories[0] = 1

    # time - months (main cycle)
    for i in range(months-1):
        # adults - saving in a
        a = 0
        if categories[alive-1] > 0:
            a = categories[alive - 1]
            categories[alive - 1] = 0

        # movement in dictionary
        for b in range(1, alive):
            categories[alive-b] = categories[alive-1-b]
            categories[alive-1-b] = 0

        # babies
        for x in range(2, alive):
            if categories[x] > 0:
                categories[0] += categories[x]
        if a > 0:
            categories[0] += a

        sum = 0
        for value in range(alive):
            sum += categories[value]
        sum_list.append(sum)
    return sum_list[-1]

print(mortal_rabbits(90, 18))

