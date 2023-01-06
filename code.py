class Solution:
    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s =''.join(str(len(list(group))) + digit
                        for digit, group in itertools.groupby(s)) 
#this method calculates the keys for each element present in iterable. 
#It returns key and iterable of grouped items
        return s

