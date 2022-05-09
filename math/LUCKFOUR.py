test = int(input())
for i in range(test):
    no = int(input())
    counter,a = 0,0
    strNo = str(no)
    while a<len(strNo):
        if(strNo[a]=="4"):
            counter+=1
        a+=1
    print(counter)