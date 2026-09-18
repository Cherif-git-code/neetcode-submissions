class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        s_nums=nums
        if s_nums[0]==s_nums[-1] :
            if s_nums[0]+s_nums[1]+s_nums[2]==0 :
                return [s_nums[:3]]
            else :
                return []
        for i in range(len(s_nums)-2) :
            if s_nums[i-1]==s_nums[i] and i>0 :
                continue
            g=i+1
            d=len(s_nums)-1
            while d>g :
                somme=s_nums[i]+s_nums[g]+s_nums[d]
                if somme>0 :
                    d=d-1
                elif somme<0 :
                    g+=1
 
                else :
                    res.append([s_nums[i], s_nums[g],s_nums[d]])
                    while g < d and s_nums[g] == s_nums[g+1]:
                        g+=1
                    while g < d and s_nums[d] == s_nums[d-1]:
                        d-=1
                    g+=1
                    d=d-1
        return res

                


        
        