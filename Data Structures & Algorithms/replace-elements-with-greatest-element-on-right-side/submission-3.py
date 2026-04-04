class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new=[]

        for i in range(0,(len(arr)-1)):
            new.append(max(arr[i+1:]))
                        
        new.append(-1)
        return new