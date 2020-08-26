newlist = [2,3,6,8,9,10]
secondlist = []


def even(newlist):
    x = 0
    while x < 6:
        if newlist[x] % 2 != 0:
            thirdlist = newlist[x]
            secondlist.append(thirdlist)
            x = x + 1 
            print(secondlist)
        else:
            x = x + 1 

even(newlist)
print(secondlist)