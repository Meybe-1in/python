
class Solution(object):
    def mergeAlternately( word1:str, word2:str):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = "" #empty string
        len1, len2 = len(word1), len(word2) #lenghts of the string
        i, j = 0 , 0           # keep track of the current positions in word1/word2

        while i < len1 and j < len2 : 
            merged += word1[i] + word2[j]
            i += 1
            j += 1

        if i < len1:             #check if you have a remaining element in word1
            merged += word1[i:]  # add the elements to the result string
        elif j < len2:           #check if you have a remaining element in word1
            merged += word2[j:]  # add the elements to the result string
        
        return merged

    print (mergeAlternately("dyn","aaa15"))

from itertools import zip_longest

def merge(self, word1: str, word2: str) -> str:
        return ''.join(a+b for a,b in zip_longest(word1, word2, fillvalue= ''))