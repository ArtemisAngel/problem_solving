
class Solution():
    def ProfitCalc(self, arr):
        buy = float('inf')
        profit = 0

    # getting buy and profit simultaneously using min and max between initial data and the one from the array of stock prices
        for i in range(len(arr)):
            buy = min(buy, arr[i])
            profit = max(profit, arr[i]-buy)

        return profit
    
if __name__ == "__main__":
    obj = Solution()
    stock = list(map(int, input("Enter the stock price data: ").split()))
    result = obj.ProfitCalc(stock)
    print("Profit = ", result)