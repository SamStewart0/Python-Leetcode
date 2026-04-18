class Solution(object):
    def maximumWealth(self, accounts):

        #init maxWealth var
        maxWealth = 0        
        
        #for each customer
        for customer in accounts:
            
            #sum the value of the current customer
            currentWealth = sum(customer)
                
            #set maxWealth to currentWealth if larger
            maxWealth = max(maxWealth, currentWealth)
        
        #return maxWealth
        return maxWealth
