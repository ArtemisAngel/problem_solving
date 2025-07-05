
# Sorting an array of 0s, 1s and 2s using Dutch Natioal Flag Algorithm

class Solution():
    def DutchAlgo(self, arr):
        n = len(arr)-1
        low = 0
        mid = 0
        high = n
        while mid<=high:
            if arr[mid]==0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low+=1
                mid+=1
            elif arr[mid]==1:
                mid+=1
            elif arr[mid]==2:
                arr[high], arr[mid] = arr[mid], arr[high]
                high-=1

        return arr
    
if __name__=="__main__":
    obj = Solution()
    arr = list(map(int, input("Enter an array of unsorted 0s, 1s, and 2s: ").split()))
    res = obj.DutchAlgo(arr)
    print(res)

# T(O) = n