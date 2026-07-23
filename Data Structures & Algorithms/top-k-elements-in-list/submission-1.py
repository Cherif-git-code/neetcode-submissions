class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dico_1={}
        dico_2=defaultdict(list)
        c=[]
        l=[]
        co=0
        for i in range(len(nums))  :
            dico_1[nums[i]]=dico_1.get(nums[i],0)+1
        for i in dico_1 :
            c.append(dico_1[i])
            dico_2[dico_1[i]].append(i)
        c=sorted(c, reverse=True)
        while co<k :
            a=dico_2[c[co]]
            for i in a :
                l.append(i)
            co+=len(a)
        return l[0:k+1]


        
