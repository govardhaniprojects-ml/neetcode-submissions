class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solHash = {}
        for i in range (0,len(nums)):
            sol = target - nums[i]
            if(solHash.get(sol) != None):
                return [solHash.get(sol),i]
            solHash[nums[i]] = i#3:0