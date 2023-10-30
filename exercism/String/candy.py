
def kidsWithCandies( candies: list[int], extraCandies: int) -> list[bool]:
    # Find out the greatest number of candies among all the kids.
    greatest = max(candies)
    #print(greater)
    
    # For each kid, check if they will have greatest number of candies
    # among all the kids.
    for x in range(len(candies)):
        result = []
        result.append(candies[x] + extraCandies >= greatest )
        print ( result)
    
kidsWithCandies([2,3,5,1,3],3)


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        result = []
        for i in range(len(candies)):            
            result.append(candies[i] + extraCandies >= maxCandies)
        return result
    