class TimeMap:

    def __init__(self):
        self.map  = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (key in self.map):
            self.map[key].append([timestamp,value])
        else:
            self.map[key] = [[timestamp,value]]

        

    def get(self, key: str, timestamp: int) -> str:
        if (key not in self.map):
            return ""
        
        l , r = 0, len(self.map[key]) - 1

        while(l <= r):
            m = (l + r) // 2
            t = self.map[key][m][0]
            if(timestamp == t):
                return self.map[key][m][1]
            elif(timestamp > t):
                l = m + 1
            else:
                r = m - 1
        
        if(m == r):
            return self.map[key][m][1]
        if(m - 1 >= 0):
            return self.map[key][m-1][1]


        return ""



        
