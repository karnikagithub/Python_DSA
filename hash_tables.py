class HashTable():
    
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]
        
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max
        
    # def add(self,key,val):
    #     h = self.get_hash(key)
    #     self.arr[h] = val
    
    ### python built-in operator for ADD
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))
        
    # def get(self,key):
    #     h = self.get_hash(key)
    #     return self.arr[h]
    
    ### python built-in operator for GET
    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    # def delete(self,key):
    #     h = self.get_hash(key)
    #     self.arr[h] = None
    
    ### python built-in operator for DELETE   
    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                
        
obj = HashTable()

# print(obj.get_hash('march 6'),'hashed value of march 6')
# print(obj.get_hash('march 11'),'hashed value of march 11')
# print(obj.get_hash('march 17'),'hashed value of march 17')
# print(obj.add('march 6',1000),'added the hashed value')
# print(obj.get('march 6'))

obj['march 6'] = 5000
obj['march 11'] = 6000
obj['march 17'] = 7000
# print(obj['march 11'])
print(obj['march 25'])
print(obj['march 17'])
# del obj['march 17']

print(obj.arr)

