class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        #3Sum with Factorials Solution
        #Time O(n^2) Space: O(n)
        
        res = 0
        table = Counter(arr)
        arr.sort()
        
        def nCk(n, k):
            return factorial(n)//(factorial(n-k)*factorial(k))
        
        for i in range(len(arr)):
            if i != 0 and arr[i] == arr[i-1]:
                continue
            r = len(arr)-1
            for j in range(i+1, len(arr)):
                if r < j:
                    break
                if j != i+1 and (arr[j] == arr[j-1] or arr[i]+arr[j]+arr[r] < target):
                    continue
                while r > j and arr[i]+arr[j]+arr[r] > target:
                    r -= 1
                if r > j and arr[i]+arr[j]+arr[r] == target:
                    ni = table[arr[i]]
                    nj = table[arr[j]]
                    nr = table[arr[r]]
                    if arr[i] == arr[r]: #all three numbers are the same
                        res += nCk(ni, 3)
                    elif arr[i] == arr[j]:
                        res += nCk(ni, 2) * nr
                    elif arr[j] == arr[r]:
                        res += ni * nCk(nj, 2)
                    else: #all numbers are different
                        res += ni * nj * nr
        
        return res % (10**9 + 7)