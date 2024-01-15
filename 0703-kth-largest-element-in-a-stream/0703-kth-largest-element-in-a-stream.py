class KthLargest:
    #Inefficient solution that sorts the list each time a number is added
    #On add(), binary search can be used to insert the new number for efficiency
    #Class can also simply track the three largest numbers and ignore the rest
    
    def __init__(self, k: int, nums: List[int]):
        self.kth = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.kth]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)