class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)

        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in counts.items():
            buckets[freq].append(num)

        results = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                results.append(num)
                if len(results) == k:
                    return results

