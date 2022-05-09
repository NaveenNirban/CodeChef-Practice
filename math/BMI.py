test = int(input())
for i in range(test):
    myInput = list(map(int, input().split()))
    m = myInput[0]
    h = myInput[1]
    bmi = m/(h*h)
    if bmi<=18:
        print(1)
    elif 19<=bmi<=24:
        print(2)
    elif 25<=bmi<=29:
        print(3)
    else:
        print(4)