import numpy as np

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = np.zeros(26, dtype = int)
        arr2 = np.zeros(26, dtype = int)
        if len(s) == len(t):
            for i in s:
                index = ord(i) - ord('a')
                arr1[index] = arr1[index] + 1
                
            for i in t:
                index = ord(i) - ord('a')
                arr2[index] = arr2[index] + 1 

            if np.all(arr1 == arr2):
                return True
        return False

        








        '''
        for i in s:
                index = ord(i) - ord('a')
                arr1[index] = arr1[index] + 1
            for i in t:
                index = ord(i) - ord('a')
                arr2[index] = arr2[index] + 1
        if np.all(arr1 == arr2):
            return True
        else:
            return False
        
        l1 = len(s)
        l2 = len(t)
        dic = {}
        if l1 == l2:
            count = 1
            for x in s:
                if dic[x] == x:
                    dic[x] = count + 1
                else:
                    dic[x] = count
        else:
            return False



         for i in range(l1):
            if s[i] > "a":
                s1[i]


        for i in range(l1-1):
            count = 1
            if s[i] == s[i+1]:
                count += 1
                dic[s[i]] = count
        print(dic)
        


        if l1 == l2: #checking whether both strings are in the same size
            for i in range(l1): 
                if s[i] not in t:
                    return False
                
            else:
                return True
        else:
            return False
            '''