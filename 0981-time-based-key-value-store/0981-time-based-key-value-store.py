class TimeMap:

    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = [(timestamp, value)]
        else:
            self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache or self.cache[key][0][0] > timestamp:
            return ""
        vals = self.cache[key]
        l = 0
        r = len(vals)-1
        
        while l <= r:
            m = (l+r)//2
            if vals[m][0] == timestamp:
                return vals[m][1]
            elif vals[m][0] > timestamp:
                r = m-1
            else:
                l = m+1
        
        l = max(0, l-1)
        return vals[l][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)