from math import gcd
class Solution:
    def gcdOfStrings(str1: str, str2: str) -> str:
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            print(" ")
        # Get the GCD of the two lengths.
        else:
            max_length = gcd(len(str1), len(str2))
            print (str1[:max_length])
        
    ''' return str1[:gcd(len(str1), len(str2))]'''

    gcdOfStrings ("ABC", "ABC")
    
    
