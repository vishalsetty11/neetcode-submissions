class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)/2
        count={}

        for i in range(len(nums)):
            val = nums[i]
            count[val] = 1+count.get(val,0)
            if count.get(val)>majority:
                return val
        return 0