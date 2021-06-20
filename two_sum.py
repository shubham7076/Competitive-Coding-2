class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Defining a dictionary for hashmap
        values = dict()

        #Looping over index and element
        for i,element in enumerate(nums):
            comp = target -element

            #If the second element in values return the index
            if comp in values:
                return [values[comp],i]
            
            #Storing the index of the element in dictionary
            values[element] =i
        return []


#This problem finds out the sum of the two elements leading to target variable to return their indices.
#Using dictionary for hashmap and time complexity O(n)
#space complexity - O(n)

b1 = Solution()
arr1= [1,3,5,6]
target = 8
print(b1.twoSum(arr1,target))