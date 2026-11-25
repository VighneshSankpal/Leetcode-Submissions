class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        idx = 0
        size = len(nums)
        moved = 0

        while idx < size - moved:


            if nums[idx] == 0:

                temp_idx = idx
                next_idx = temp_idx+1

                while next_idx < size :
                    
                    nums[temp_idx], nums[next_idx] = nums[next_idx], nums[temp_idx]

                    temp_idx +=1
                    next_idx +=1

                moved+= 1

            else:
                idx +=1