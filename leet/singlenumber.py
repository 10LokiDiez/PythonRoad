class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for num in nums:
            if nums.count(num) == 1:
                return num
    
sol = Solution()
number = sol.singleNumber([2,2,1])
print(number)