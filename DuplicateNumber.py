# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and using only constant extra space.

from typing import List

class Solution():
    def FindDuplicate(self, arr: List[int]) -> int:
        n = len(arr)
        freq = [0]*(n)
        
        for i in range(n):
            if freq[arr[i]]==0:
                freq[arr[i]]+=1
            else:
                return arr[i]

        return 0
    
if __name__=="__main__":
    obj = Solution()
    arr = list(map(int, input("Enter an array of randomly arranged consecutive integers with a duplicate integer: ").split()))
    res = obj.FindDuplicate(arr)
    print("The Duplicate integer is: ",res)

# T(O) = n