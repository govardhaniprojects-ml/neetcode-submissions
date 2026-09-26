class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash={}
        tHash={}
        for charItem in s:
            if(sHash.get(charItem)):
                sHash[charItem] = sHash[charItem]+1
            else:
                sHash[charItem] = 1
        for charItem in t:
            if(tHash.get(charItem)):
                tHash[charItem] = tHash[charItem]+1
            else:
                tHash[charItem] = 1
            
        for keyItem in sHash:
            if(sHash[keyItem] != tHash.get(keyItem)):
                return False
        for keyItem in tHash:
            if(tHash[keyItem] != sHash.get(keyItem)):
                return False
        return True
        
print(Solution().isAnagram("a","ab"))