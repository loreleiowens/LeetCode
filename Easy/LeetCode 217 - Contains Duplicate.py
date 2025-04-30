class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    # Initial answer - unsuccessful in some tests
      # nums.sort()
      # first, second = 0, 1
      # while second < len(nums):
      #   if nums[first] == nums[second]:
      #     return True
      #   else:
      #     return False
      #   second += 1
      #   first += 1
        
    # NeetCode answer
        # numSet = set()
        # for n in nums:
        #     if n in numSet:
        #         return True
        #     numSet.add(n)
        # return False

    # Separate set answer
        for n in range(len(nums)):
            if len(set(nums)) == len(nums):
                return False
            else:
                return True


