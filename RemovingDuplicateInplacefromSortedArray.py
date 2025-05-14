#Time Complexity = O(n)

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for i in range (1,len(nums)):   # T(n) = O(n)
            if nums[i]!=nums[k]:
                k+=1
                nums[k] = nums[i]
                
        return k+1

if __name__ == "__main__":
    n = list(map(int, input().split(",")))
    sol = Solution()
    k = sol.removeDuplicates(n)
    for i in range(k):
        print(n[i], end=",")
