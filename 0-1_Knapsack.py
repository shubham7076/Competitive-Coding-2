
def knapsack1(W,value,WT,n):

    #Base condition
    if n==0 or WT == 0:
        return 0

    if (W[n-1] > WT):
        return knapsack1(W,value,WT,n-1)
                
    else:
        return max(value[n-1]+ knapsack1(W,value,WT-W[n-1],n-1),knapsack1(W,value,WT,n-1))
            
#Driver code
value = [30,40,50,60]
W = [10,20,30,40]
WT=100
N = len(W)
print(knapsack1(W,value,WT,N))


#The knapsack problem provides the max possible weight that can be placed in a knapsack with a certain weight and values correspond to each weight.Using recursion we calcuate the max possible output.
#Time complexity - O(N*WT)
#Space complexity - O(N*WT)


def knapsack2(W,value,WT,n):

    #Base condition
    if n==0 or WT == 0:
        return 0

    #Defining the matrix array
    temp = [[-1 for i in range(WT+1)] for j in range(n+1)]

    if temp[n][WT]!= -1:
        return t[n][WT]

    if (W[n-1] > WT):
        temp[n][WT] = knapsack2(W,value,WT,n-1)
        return temp[n][WT]
                
    else:
        temp[n][WT]= max(value[n-1]+ knapsack2(W,value,WT-W[n-1],n-1),knapsack2(W,value,WT,n-1))
        return temp[n][WT]
    
print(knapsack2(W,value,WT,N))

#Using memoization to reduce the redundant cases
#Time complexity - O(N*WT)
#Space complexity - O(N*WT)