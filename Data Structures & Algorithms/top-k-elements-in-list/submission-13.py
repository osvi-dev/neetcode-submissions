from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frecuency = dict(Counter(nums))
        order_dict = dict(sorted(frecuency.items(), key=lambda x: x[1], reverse=True))
        # print(order_dict.keys())
        answer = list(order_dict.keys())
        return answer[:k]