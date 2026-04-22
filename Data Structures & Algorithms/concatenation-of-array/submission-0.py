class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums1  = [0]*(2*n)

        for i in range(n):
            nums1[i] = nums[i]
            nums1[i+n]=nums[i]
        return nums1
        