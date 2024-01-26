class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize result array
        result = [1] * n
        
        # Calculate prefix to the left of each element
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
            
        # Calcualte postfix to the right of each element
        postfix = 1
        for i in range(n -1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
            
        
        