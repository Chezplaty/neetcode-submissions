from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        search_list = self.hashMap[key]
        l, r = 0, len(search_list) - 1
        res = ""

        while l <= r:
            mid = (l+r) // 2
            curr_time = search_list[mid][0]

            if curr_time <= timestamp:
                res = search_list[mid][1]
                l = mid + 1
            
            else:
                r = mid - 1
        
        return res

