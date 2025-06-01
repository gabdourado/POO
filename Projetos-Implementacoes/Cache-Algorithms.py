class Cache:
  
    def __init__(self, size: int) -> None:
        
        self.size_cache = size
        self.space_cache = [None for _ in range(size)]
        self.number_used = [0 for _ in range(size)]
        self.algorithms = {'1': self.FIFO, '2': self.LFU, '3': self.LRU,'4': self.Random}

    def FIFO(self, data: int) -> int:

        if data in self.space_cache:
            return 1

        if self.space_cache.count(None) == 0:
            self.space_cache.pop(0)
            self.space_cache.append(data)
            return 0

        idx = self.space_cache.index(None)
        self.space_cache[idx] = data

        return 0

    def LRU(self, data: int) -> int:

        if data in self.space_cache:
            idx = self.space_cache.index(data)
            self.number_used[idx] += 1
        
            return 1

        if self.space_cache.count(None) == 0:  
            idx = self.number_used.index(min(self.number_used))
        else:
            idx = self.space_cache.index(None)
        
        self.space_cache[idx] = data
        self.number_used[idx] = 1

        return 0

    def LFU(self, data: int) -> int:
        
        if data in self.space_cache:
            
            if self.space_cache.count(None) != 0:
                self.space_cache.remove(data)
                idx = self.space_cache.index(None)
                self.space_cache.insert(idx, data)
                
                return 1
            
            self.space_cache.remove(data)
            self.space_cache.append(data)

            return 1
    
        if self.space_cache.count(None) == 0:
            self.space_cache.pop(0)
            self.space_cache.append(data)
            
            return 0
        
        idx = self.space_cache.index(None)
        self.space_cache[idx] = data

        return 0

    def Random(self, data: int) -> int:
        
        if data in self.space_cache:
            return  1

        if self.space_cache.count(None) == 0:
            idx = self.space_cache.index(random_data(self.space_cache))
            self.space_cache.pop(idx)
            self.space_cache.insert(idx, data)
            return 0

        idx = self.space_cache.index(None)
        self.space_cache.insert(idx, data)
        self.space_cache.pop(idx + 1)
        
        return 0

from random import choice

def random_data(data_set: list) -> int:
   while True:
      data = choice(data_set)

      if data:
         return data

def hit_or_miss(out: int) -> None:
    if out:
        print("Cache Hit")
    else:
        print("Cache Miss")

if __name__ == "__main__":
    
    print("1 - FIFO\n2 - LRU\n3- LFU\n4 - Random")
    option = input("Chose your algorithm: ")
    
    size_cache = int(input("Size of your Cache: "))
    num_interation = int(input("The number of itaration: "))

    cache = Cache(size_cache)

    if option not in cache.algorithms:
        print("Value Invalid!")
        exit

    for _ in range(num_interation):
        data = (input("Data: "))

        if not data.isdigit():
            print("Data invalide")
            continue

        out = cache.algorithms[option](data)
        print(cache.space_cache, end=' -> ')
        hit_or_miss(out)