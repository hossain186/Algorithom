n = int(input())

nums = [True for i in range(n+1)]
# initial indexing value 2
j = 2

while j*j<=n:

     if nums[j]== True:

         for i in range(j*j, n+1 , j):
             nums[i] = False
     j+=1


for i in range(2, n+1):

    if nums[i]:
        print(i)