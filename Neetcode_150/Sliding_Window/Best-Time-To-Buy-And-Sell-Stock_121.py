class Solution(object):
    def maxProfit(self, prices):

        #check first day

        maxProfit = 0
        lowestSeen = prices[0]

        #for each value in prices
        for num in prices:

            #if num is lowest save it to lowestSeen
            if num<lowestSeen:
                
                lowestSeen = num

            #if max profit is higher make it maxProfit
            elif  num-lowestSeen>maxProfit:

               maxProfit = num-lowestSeen

    
        return maxProfit
