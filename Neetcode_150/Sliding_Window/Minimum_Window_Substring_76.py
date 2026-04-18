from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:


        if len(s) < len(t):

            return ""

        #get our counts for T

        t_counts = defaultdict(int)
        
        for letter in t:

            t_counts[letter] += 1

        #get our need value

        need = len(t_counts)

        #init our have value and current_window counts

        have = 0
        current_window = defaultdict(int)

        #init our L pointer and min_len value and result indicies

        L = 0
        min_len = float("inf")
        res_index = [0,0]

        for R in range(len(s)):

            current_window[s[R]] += 1

            #if the char counts are the same we increment our have counter

            if current_window[s[R]] == t_counts[s[R]]: 
                have += 1

            #now while need == have we contract our window

            while need == have:

                #get current window length and compare to min length
                #store indices for result

                current_window_len = (R-L+1)

                if current_window_len < min_len:

                    min_len = current_window_len
                    res_index = [L,R]

                #get the char we are removing 

                removed_char = s[L]

                #if the char leaving the window is in t_counts and is matching the t_count value exactly
                #its breaking our criteria so decrement have

                if removed_char in t_counts and current_window[removed_char] == t_counts[removed_char]:
                    have -= 1

                #decrement our counts in current window and increment L 

                current_window[removed_char] -= 1
                L += 1
        
        L,R = res_index
        
        return s[L:R+1] if min_len != float("inf") else ""
