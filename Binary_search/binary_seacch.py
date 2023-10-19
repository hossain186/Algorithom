def binary_search(list , target):

    low = 0
    high = len(list)-1

    while low<=high:

        mid = (low+high)//2
        gucess = list[mid]

        if gucess == target:
            return mid
        elif gucess >target:
            high = mid- 1
        else:
            low  = mid+1

    return  None


print(binary_search([1,2,3,4,5,6],0))