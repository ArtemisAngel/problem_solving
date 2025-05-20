# Leader = an element whose value is strictly greater than all elements to its right
# T(O) = N


class Solution:
    def leaders(self, nums):
        max = nums[-1]
        leader = []
        leader.append(nums[-1])

        for i in range(len(nums)-2, -1, -1):
            if nums[i]>max:
                leader.append(nums[i])
                max = nums[i]

        for i in range(len(leader)//2):
            leader[i], leader[len(leader)-1-i] = leader[len(leader)-1-i], leader[i]

        return leader
    
if __name__=="__main__":
    obj = Solution()
    arr = list(map(int, input("Space Separated Values: ").split()))
    res = obj.leaders(arr)
    print(res)