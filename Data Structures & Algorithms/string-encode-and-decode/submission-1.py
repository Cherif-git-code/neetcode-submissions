class Solution:

    def encode(self, strs: List[str]) -> str:
        mots=str()
        for i in strs :
            mots+=i+"s!!!"
        return mots


    def decode(self, s: str) -> List[str]:
        l=[]
        c=str()
        i=0
        while i<len(s) :
            if s[i]=='s' and s[i+1]=="!" and s[i+2]=="!":
                l.append(c)
                c=str()
                i+=4
            else :
                c+=s[i]
                i+=1
        return l


            




