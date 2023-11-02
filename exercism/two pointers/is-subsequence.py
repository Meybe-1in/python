class Solution:
    def isSubsequence(s: str, t: str) -> bool:
        if len(s) > len(t):return False
        if len(s) == 0:return True
        subsequence=0
        for i in range(0,len(t)):
            if subsequence <= len(s) -1:
                print(s[subsequence])
                if s[subsequence]==t[i]:

                    subsequence+=1
        print  (subsequence == len(s) )
    isSubsequence("abc","afcyhb")
    
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t) :
            return False
        if len(s) == 0:
            return True
        
        l = 0
        for i in range(len(t)):
            if l <= len(s) - 1:
                if t[i] == s[l]:
                    l += 1
        
        return l == len(s)
    
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ids, idt = 0,0
        while ids < len(s) and idt < len(t):
            if t[idt] == s[ids]:
                idt += 1
                ids += 1
            else:
                idt += 1
        
        if ids != len(s):
            return False
        
        return True