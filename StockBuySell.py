
class Solution():
    def ProfitCalc(self, arr):
        buy = arr[0]
        sell = 0
        buy_date = 0

        # Buying stock at lowest price
        for i in range(len(arr)-1):
            if arr[i]<buy:
                buy = arr[i]
                buy_date = i
        
        #Selling stock at highest price
        for i in range(buy_date, len(arr)):
            if arr[i]>sell:
                sell = arr[i]

        #calculating profit
        profit = sell - buy

        if profit<0:
            return 0

        return profit
    
if __name__ == "__main__":
    obj = Solution()
    stock = list(map(int, input("Enter the stock price data: ").split()))
    result = obj.ProfitCalc(stock)
    print("Profit = ", result)