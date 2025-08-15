class TimeMap:

    def __init__(self):
        self.dic = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = [(value, timestamp)]
        else:
            self.dic[key].append((value, timestamp))


        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        target = timestamp
        lst = self.dic[key]
        l, r = 0, len(lst) - 1
        while l < r:
            m = (l + r) // 2
            if timestamp >= lst[m][1]:
                l = m + 1
            else:
                r = m
        if l == 0:
            return ""
        return lst[l - 1][0]
            
                
tm = TimeMap()
tm.set("foo", "bar", 1)
tm.get("foo", 1)   # ➤ "bar"
tm.get("foo", 3)   # ➤ "bar" (vì thời điểm gần nhất <= 3 là 1)
tm.set("foo", "bar2", 4)
tm.get("foo", 4)   # ➤ "bar2"
tm.get("foo", 5)   # ➤ "bar2" 
        
