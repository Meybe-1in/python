class Solution:
    def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        check=m+n-1
        i = m-1
        j = n-1
        while (i>=0 or j>=0) and check>=0:
            if i>=0 and j>=0:
                if nums1[i]<nums2[j]:
                    nums1[check]=nums2[j]
                    j-=1
                    check-=1
                else:
                    nums1[check]=nums1[i]
                    i-=1
                    check-=1
            elif i>=0:
                check-=1
            else:
                nums1[check]=nums2[j]
                j-=1
                check-=1


#Will use back-tracking. 
# We iterate for array1 from (m+n-1) to 0 and m-1 to 0, for Array2 n-1 to 0.
# compare the value of each iteration and place the value at nums1.

#Complexity
#Time complexity: O(m+n) 40ms
#Space complexity: O(1) 16.13