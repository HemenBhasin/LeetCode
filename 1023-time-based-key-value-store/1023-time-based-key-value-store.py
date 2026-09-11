class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        temp=self.map.get(key, [])
        low, high = 0, len(temp) - 1
        ans=""
        while low <= high:
            
            mid = (low + high) // 2

            if temp[mid][0]<=timestamp:
                ans=temp[mid][1]
                
                low = mid + 1
            else:
                high = mid - 1
        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)