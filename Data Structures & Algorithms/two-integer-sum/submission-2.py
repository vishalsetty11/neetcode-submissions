class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            addend = target - nums[i]
            if addend in nums:
                j = nums.index(addend)
                if i != j:
                    return sorted([i,j])
        return []