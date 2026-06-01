class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #seen is an empty (hash) set at the beginning

        for n in nums: 
            if n in seen: 
                return True
            seen.add(n)

        return False
