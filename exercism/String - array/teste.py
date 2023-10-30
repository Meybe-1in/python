def merged_string_alternately (word1:str, word2:str):
    """merged string alternately
    
    Args:
        word1 (str): first word to merged
        word2 (str): second word to merged
        
    Example:
        input:"abc","12356"
        output:"a1b2c356"
    """
    merged=""
    len1 , len2 = len(word1), len(word2)
    i , j = 0 , 0
        
    while i < len1 and j < len2:
        merged += word1[i] + word2[j]
        i += 1
        j += 1
        
    if i < len1:
        merged += word1[i:]
    elif j < len2:
        merged += word2[j:] 
    
    print (merged)
    
merged_string_alternately ("135", "24678")

#adbecfgh