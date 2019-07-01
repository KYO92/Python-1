list1 = []
list2 = []
list3 = []

for i in range(0,5) :
    for k in range(0,4) :
        for l in range(1,10) :
            aa = l * value
            result = 'l X 1 = aa'
            list1.append(result1)
        list2.append(list1)
        list3.append(list2)
        list1 = []
    list3.append(list2)
print(list3)
for i in range(0,5) :
    for k in range(0,4) :
        for l in range(0,9) :
            print(list3[i],[k],[l])
        print()