class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicroman ={
        "I":1,
         "V":5,
         "X":10,
         "L":50,
         "C":100,
         "D":500,
         "M":1000,}
        sum = 0
        for i in range(len(s)):
            c = s[i]
            if s[i+1]:
                if dicroman[s[i]] > dicroman[s[i+1]]:
                    sum += dicroman[s[i]]
        return sum
        
solu = Solution()
num = solu.romanToInt("XIII")
print(num)