def findSmallest(arr):

    smallest = arr[0] #just initial that,, suppose arr[0] is the smallest value
    smallnumber_index = 0 #initial index value

    #now chack array value accroding smallest value

    for i in range(len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallnumber_index = i

    return smallnumber_index


new = []

a = [2,1,4,2,6,4]
for i in range(len(a)):

    small = findSmallest(a)
    new.append(small)
    a.remove(small)

print(new)