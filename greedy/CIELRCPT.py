def greedy(myInput):
    a = 1
    counter = 0
    while counter<11:
        a = a * 2
        counter+=1
        #print("counter ",counter)
        if (a<=myInput):
            continue
        if a>myInput:
            a = a//2
            break
    return a

test = int(input())
for i in range(test):
    myInput = int(input())
    counter = 0
    while myInput!=0:
        myInput = myInput - greedy(myInput)
        counter+=1
    print(counter)