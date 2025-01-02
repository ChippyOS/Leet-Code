 class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sequence = set(nums)

        output = 0

        for num in sequence:
            if (num - 1) not in sequence:
                length = 1
                while (num + length) in sequence:
                    length += 1
                output = max(length, output)
        return output

