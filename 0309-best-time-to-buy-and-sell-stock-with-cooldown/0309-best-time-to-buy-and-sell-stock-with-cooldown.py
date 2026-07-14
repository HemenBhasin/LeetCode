class Solution(object):
    def maxProfit(self, prices):      
        n=len(prices)
        if n <2:
            return 0       
        hold=-float('inf') 
        sold=0
        rest=0
        for price in prices:
            next_hold=max(hold,rest-price) #We either keep holding what we have or we buy a new stock from a 'rest' state
            next_sold=hold+price #reach the 'sold' state by selling a stock we are currently holding
            next_rest=max(rest,sold) #either keep resting or we transition into rest because we sold a stock yesterday
            sold=next_sold
            rest=next_rest
            hold=next_hold
        return max(sold,rest)    