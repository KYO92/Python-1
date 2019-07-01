list1 = []
list2 = []
list3 = []
value =1
for i in range(0,5) :
    for k in range(0,4) :
        list1.append(value)
        value += 1
    list2.append(list1)
    list1 = []

for i in range(0,5) :
    for k in range(0,4) :
        print("%3d", "x", "%3d", "=" %3d % list2[i][k], end = " ")
    print("")
