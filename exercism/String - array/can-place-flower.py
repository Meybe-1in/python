class Solution:
    def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        print(True)
      
        return count >= n
        print(False)
    
    canPlaceFlowers ([1,0,1,0,1,0,0,0,0,0,0] , 3 )
    
    
"""class Solution:
    def canPlaceFlower( flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    print (True)
        print (False)
 
    canPlaceFlower ([1,0,1,0,1,0,0,0,0,0,0] , 1)"""