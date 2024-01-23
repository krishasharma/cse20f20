#Quiz4Question2

L = [1, 2, 3, 4, 5, 6, 7, 8]
def splitList(L): 
    ev_li = [] 
    od_li = [] 
    for i in L: 
        if (i % 2 == 0): 
            ev_li.append(i) 
        else: 
            od_li.append(i) 
    print("Even lists:", ev_li) 
    print("Odd lists:", od_li)

splitList(L)
