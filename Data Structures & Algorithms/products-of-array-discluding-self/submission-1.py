class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c=1
        compteur_de_zeros=0
        c0=1
        for i in range (len(nums)) :
            c*=nums[i]
            if nums[i]==0 :
                compteur_de_zeros+=1
                c0*=1
            else :
                c0*=nums[i]
        if compteur_de_zeros>1 :
            return [0]*len(nums)
        
        l=[int(c/nums[i])  if nums[i]!=0 else int(c0) for i in range(len(nums))]
        return l

        