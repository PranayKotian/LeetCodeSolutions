class NumArray:

    def __init__(self, nums: List[int]):
        self.sumUpTo = []
        cur = 0
        for n in nums:
            cur += n
            self.sumUpTo.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sumUpTo[right]
        else:
            return self.sumUpTo[right] - self.sumUpTo[left-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)