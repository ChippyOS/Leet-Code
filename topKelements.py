class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        freqList = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freqList[cnt].append(num)

        res = []
        for i in range(len(freqList) - 1, 0, -1):
            for num in freqList[i]:
                res.append(num)
                if len(res) == k:
                    return res