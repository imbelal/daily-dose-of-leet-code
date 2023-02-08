class TimeMap:
    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashMap:
            arr = self.hashMap.get(key)
            if timestamp > arr[-1][-1]:
                return arr[-1][0]
            elif timestamp < arr[0][-1]:
                return ""
            else:
                l, r = 0, len(arr) - 1
                res = ""
                resTimeStamp = 0
                while l <= r:
                    mid = (l + r) // 2
                    if arr[mid][-1] < timestamp:
                        if resTimeStamp < arr[mid][-1]:
                            resTimeStamp = arr[mid][-1]
                            res = arr[mid][0]
                        l = mid + 1
                    elif arr[mid][-1] > timestamp:
                        r = mid - 1
                    else:
                        return arr[mid][0]
                return res
        return ""


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("FOO", "BAR", 1)
obj.set("FOO", "BAR2", 2)
obj.set("FOO", "BAR3", 3)
obj.set("FOO", "KKK4", 4)
obj.set("FOO", "KKK8", 8)
obj.set("FOO", "KKK10", 10)
print(obj.get("FOO", 7))
