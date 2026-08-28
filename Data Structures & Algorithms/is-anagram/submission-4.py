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