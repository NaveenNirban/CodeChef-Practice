import math

test = int(input())
for i in range(test):
    no = int(input())
    tenPercentDiscount = math.floor((10 / 100) * no)

    flatDiscount = 100
    if (tenPercentDiscount >= flatDiscount):
        print(tenPercentDiscount)
    else:
        print(flatDiscount)
    # tenPercentDiscount>=flatDiscount if print(tenPercentDiscount) else print(flatDiscount)