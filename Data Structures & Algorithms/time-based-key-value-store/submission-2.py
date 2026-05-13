class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.dic:
            return ""
        values = self.dic[key]


        l, r = 0, len(values) - 1
        res = ""

        while l <= r:
            mid = (l+r)//2

            time_mid = values[mid][1]

            if time_mid <= timestamp:
                res = values[mid][0]
                l = mid + 1
            elif time_mid > timestamp:
                r = mid - 1

        return res

    

        
