
class Solution():
    def Alternate(self, arr):
        n = len(arr)
        alt_arr = []
        pos = []
        neg = []

        
        # separated the negative and the positive inputs
        for i in range(n):
            if arr[i]<0:
                neg.append(arr[i])
            else:
                pos.append(arr[i])

        # Assumption: equal positive and negative integers randomly arranged in the input array
        for i in range(int(n/2)):
            alt_arr.append(pos[i])
            alt_arr.append(neg[i])
        
        return alt_arr
    
if __name__ == "__main__":
    obj = Solution()
    IntArray = list(map(int, input("Enter negative and positive numbers (equal in strength): ").split()))
    result = obj.Alternate(IntArray)
    print(result)