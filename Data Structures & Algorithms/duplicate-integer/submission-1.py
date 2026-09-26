class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = {}
        for i in nums:
            if(data.get(i)):
                return True
            data[i]=1
        return False
        