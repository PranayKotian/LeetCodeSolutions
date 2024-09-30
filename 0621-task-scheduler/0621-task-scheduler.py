class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #Counter Solution
        #Time: O(n) Space: O(n)
        
        c = Counter(tasks)
        mostCommon = c.most_common()
        a = mostCommon[0][1]
        
        b = 1
        for let,f in mostCommon[1:]:
            if f == a:
                b += 1
            else:
                break
        
        return max(len(tasks), (n+1)*(a-1) + b)