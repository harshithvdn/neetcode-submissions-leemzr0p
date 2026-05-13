class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftmin=prices[0]
        ind=0
        profit=0
        demoprofit=0

        for i in prices:
            if prices[ind]<leftmin:
                leftmin=prices[ind]
            else:
                demoprofit=prices[ind]-leftmin
                if demoprofit> profit:
                    profit=demoprofit
            ind +=1
        

        return profit






        