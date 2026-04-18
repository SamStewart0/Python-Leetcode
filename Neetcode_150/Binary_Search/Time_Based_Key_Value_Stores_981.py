
class TimeMap:

    def __init__(self):

        #creates a dictionary where value defaults to a list 

        self.TimeMap = defaultdict(list)
        
    
    def set(self, key: str, value: str, timestamp: int) -> None:

        #append our key and value pair to the dict

        self.TimeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        #if they doesnt exist return an empty string
        
        if key not in self.TimeMap:

            return ""

        values = self.TimeMap[key]

        #bisect performs binary search for timestamp
        #because bisect_right finds the insertion point we set index 1 of the tuple a large value
        #to force the correct value (timestamp or previous closest timestamp) to be i-1

        i = bisect.bisect_right (values ,(timestamp, chr(127)))

        return values[i-1][1] if i > 0 else ""

        
        '''
        Normal Binary Search

        #result string

        res = ""

        #set pointers for binary search
        
        L = 0
        R = len(self.TimeMap[key])-1

        while L <= R:

            #perform binary search to find correct timestamp

            mid = (L+R) // 2

            if self.TimeMap[key][mid][0] <= timestamp:

                res = self.TimeMap[key][mid][1]

                L = mid + 1

            else:

                R = mid - 1

        return res
        '''
