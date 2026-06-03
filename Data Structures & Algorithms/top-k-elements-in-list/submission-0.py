class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}
        for n in nums: 
            if n in nums_count: 
                nums_count[n] += 1
            else: 
                nums_count[n] = 1 

            
        sorted_items = sorted(nums_count.items(), key = lambda x :x[1], reverse = True)

        result = []

        for item in sorted_items[:k]:
            result.append(item[0])

        return result 