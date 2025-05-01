class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      # Initial try - unsuccessful 
        # maxLen = 0
        # sCheck = ''

        # for i in range(len(s)):
        #     if s[i] not in sCheck:
        #         sCheck += s[i]
        #         maxLen += 1
            
        # return maxLen

     # Proper solution w/ comments
        l = maxLen = 0
        charSet = set()
        
        for r in range(len(s)):
            while s[r] in charSet: 
                charSet.remove(s[l]) # Remove duplicate & push sliding window over one
                l += 1 # add 1 to prevent maxLen increasing

            charSet.add(s[r]) # Checks if r is in charSet - adds back in duplicate value as sliding window updated to exclude
            maxLen = max(maxLen, r - l + 1) # Updates maxLen everytime unique value appears
        
        return maxLen
