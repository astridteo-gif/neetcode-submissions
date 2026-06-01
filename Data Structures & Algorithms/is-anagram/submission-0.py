class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {} #initializing a hash table for s
        t_count = {} #initializing a hash table for t

        for char in s: 
            if char in s_count:
                s_count[char] += 1
            else: 
                s_count[char] = 1 

        for char in t: 
            if char in t_count:
                t_count[char] += 1
            else: 
                t_count[char] = 1 

        if t_count == s_count: 
            return True
        else: 
            return False