class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minarr=prices[0]
        maxprofit=0
        i=1
        for i in range(len(prices)):
            minarr=min(minarr,prices[i])
            profit=prices[i]-minarr
            if profit>=maxprofit:
                maxprofit=profit
            
        return maxprofit 