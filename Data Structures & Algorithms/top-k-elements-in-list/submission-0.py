class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}

        if len(nums) < 1:
            return []

        for n in nums:

            count_dict[n] = count_dict.get(n, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]

        for key, value in count_dict.items():
            freq[value].append(key)

        res = []

        for i in range(len(freq)-1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

            