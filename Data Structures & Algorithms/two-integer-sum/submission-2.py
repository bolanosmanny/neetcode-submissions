class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {}

        for index, num in enumerate(nums):
            difference = target - num

            if(difference in counts):
                return [counts[difference], index]

        
            counts[num] = index

                    








