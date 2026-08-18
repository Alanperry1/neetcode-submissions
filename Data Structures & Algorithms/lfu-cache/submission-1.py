class LFUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={} #key:[value,freq,recency]
        self.recent=0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.recent+=1
        self.cache[key][1]+=1
        self.cache[key][2]=self.recent
        return self.cache[key][0]

        

    def put(self, key: int, value: int) -> None:
        if self.capacity<=0: return 
        self.recent+=1 
        if key in self.cache:
            self.cache[key][0]=value
            self.cache[key][1]+=1
            self.cache[key][2]=self.recent
            return 

        if len(self.cache)>=self.capacity:
            rem_key=min(self.cache, key=lambda k:(self.cache[k][1],self.cache[k][2]))
            del self.cache[rem_key]

        self.cache[key]=[value,1,self.recent]
            



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)