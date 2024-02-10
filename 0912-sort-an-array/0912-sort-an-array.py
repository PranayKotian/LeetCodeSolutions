class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, L, M, R):
            left = arr[L:M+1]
            right = arr[M+1:R+1]
            i = L
            lp = rp = 0
            
            while lp < len(left) and rp < len(right):
                if left[lp] < right[rp]:
                    arr[i] = left[lp]
                    lp += 1
                else:
                    arr[i] = right[rp]
                    rp += 1
                i += 1
            while lp < len(left):
                arr[i] = left[lp]
                lp += 1
                i += 1
            while rp < len(right):
                arr[i] = right[rp]
                rp += 1
                i += 1
        
        def mergeSort(arr, l, r):
            if l == r:
                return arr
            
            m = (l+r)//2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
            return arr
        
        return mergeSort(nums, 0, len(nums)-1)