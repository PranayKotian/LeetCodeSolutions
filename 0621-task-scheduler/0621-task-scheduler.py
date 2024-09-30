class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #Counter Solution
        #Time: O(n) Space: O(n)
        
        c = Counter(tasks).values()
        a = max(c)
        b = list(c).count(a)
        return max(len(tasks), (n+1)*(a-1) + b)