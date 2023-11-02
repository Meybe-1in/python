class Solution:
    def moveZeroes(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
class Solution:
    def moveZeroes(nums: list[int]) -> None:
        index = 0  
       
        for i in range(len(nums)):
            if nums[i] != 0:
                # If the current element is non-zero, swap it with the element at index
                # This effectively moves non-zero elements to the beginning of the list
                nums[i], nums[index] = nums[index], nums[i]
                index += 1 
        print (nums)   
    moveZeroes([2,0,2,3,0,1])        
     
'''class Solution:
    def moveZeroes(nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1'''
                
def moveZeroe(nums: list[int]) -> None:
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[index] == 0:
                nums[i],nums[index] = nums[index],nums[i]
            if nums[index] != 0:
                index += 1
        print(nums)
        
moveZeroe([2,0,2,3,0,7])  