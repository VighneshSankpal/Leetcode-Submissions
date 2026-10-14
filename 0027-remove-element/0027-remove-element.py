class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        current = 0
        end = len(nums)-1
        
        while current <= end :
            if nums[current] == val :

                nums[current] = nums[end]
                nums[end] = val

                end -= 1
            
            else:
                current +=1
        

        return current

        