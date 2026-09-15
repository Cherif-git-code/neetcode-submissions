class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            d[target-nums[i]]=i
        for j in range(len(nums)) :
            if nums[j] in d :
                if j>d[nums[j]] :
                    return [d[nums[j]], j]
                elif j<d[nums[j]] :
                    return [j, d[nums[j]]]
        return

 

        