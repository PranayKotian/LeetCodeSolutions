class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        #Stack Solution
        #Time: O(n) Space: O(n)
        
        stack = [pushed[0]]
        i = 1
        
        for popVal in popped:
            while i < len(pushed) and (not stack or popVal != stack[-1]):
                stack.append(pushed[i])
                i += 1
            if popVal != stack[-1]:
                return False
            stack.pop()
        return True