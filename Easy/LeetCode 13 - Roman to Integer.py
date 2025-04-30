class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary of all the various symbols & number equiv.
        numDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0

        for i in range(len(s)):
            if i+1 < len(s) and numDict[s[i]] < numDict[s[i+1]]:
                num -= numDict[s[i]]
            else:
                num += numDict[s[i]]
        return num
