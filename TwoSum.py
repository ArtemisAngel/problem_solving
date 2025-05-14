class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        res = []
        for ind, val in enumerate(nums):
            tar = target - val
            if tar in hashmap:
                return sorted([hashmap[tar], ind])
            else:
                hashmap[val] = ind

if __name__=="__main__":
    obj = Solution()
    arr = list(map(int, input("Space Separated Values: ").split(" ")))
    target = int(input())
    res = obj.twoSum(arr, target)
    print(res)