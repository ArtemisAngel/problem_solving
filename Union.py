# T(O) = N+M

class Solution:
    def unionArray(self, nums1, nums2):
        s = set()
        nums = []
        for i in nums1: #O(n)
            s.add(i)
        for i in nums2: #O(m)
            s.add(i)
        for i in s: #O(n+m)
            nums.append(i)
        return nums

if __name__=="__main__":
    obj = Solution()
    arr1 = list(map(int, input("Space Separated Values: ").split()))
    arr2 = list(map(int, input("Space Separated Values: ").split()))
    ans = obj.unionArray(arr1, arr2)
    print(ans)

