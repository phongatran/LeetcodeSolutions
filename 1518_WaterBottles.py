class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # 1) Simply drink all the bottles on the first step
        # 2) Create a while loop that accounts for exchanging at given rate
        # If the number of empty bottles is less than the exchange rate, then stop the count
        # because this means that bottles can no longer be redeemed for new drinks
        
        totalBottles = numBottles
        emptyBottles = numBottles
        
        while (emptyBottles >= numExchange):
            exchBottles = floor(emptyBottles/numExchange)
            emptyBottles = emptyBottles - exchBottles*numExchange
            totalBottles += exchBottles
            emptyBottles = emptyBottles + exchBottles
            
        return totalBottles