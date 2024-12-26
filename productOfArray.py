 class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ret = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                
                if i != j:
                    ret[i] *= nums[j]


        

        return ret

