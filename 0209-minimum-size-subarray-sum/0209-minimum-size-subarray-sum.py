class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        min_lenght = len(nums) + 1
        sub_sum = 0


        while right < len(nums):

            sub_sum += nums[right]

            while sub_sum >= target:

                if min_lenght > right - left + 1:
                    min_lenght = right - left + 1
                
                sub_sum -= nums[left]
                left += 1

            right +=1

        
            
    
        return 0 if min_lenght == len(nums)+1 else min_lenght