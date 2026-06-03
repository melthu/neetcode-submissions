class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 101
        best = 0

        for i in range(len(prices)):
            profit = prices[i] - buy
            print(profit)
            best = max(best, profit)
            print(best)
            buy = min(buy, prices[i])
            print(buy)
            print()

            

        return best
            
            
            


            
        