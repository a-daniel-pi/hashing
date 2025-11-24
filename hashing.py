# Author: Daniel Pierce

import csv, time

def getHash(string):
    result = 5381
    for n, i in enumerate(string):
        result = (result * 33 + ord(i))%(2**31-1)
    return result

class DataItem:
    def __init__(self, line):
        self.movie_name = line[0]
        self.genre = line[1]
        self.release_date = line[2]
        self.director = line[3]
        self.revenue = float(line[4][1:])
        self.rating = float(line[5])
        self.duration = int(line[6])
        self.production_company = line[7]
        self.quote = line[8]
        
    def __repr__(self):
        return self.movie_name
        
class DataItemEntry:
    def __init__(self, item):
        self.item = item
        self.next = None
        
    def __repr__(self):
        return f"{self.item} -> {self.next}"
        
class HashTable:
    def __init__(self, length):
        self.ls = [None] * length
        self.length = length
        self.collisions = 0
        self.unused = length
        
    def add(self, item, key):
        index = getHash(key)%self.length
        if self.ls[index]:
            self.resolveCollision(item, index)
        else:
            self.ls[index] = DataItemEntry(item)
            self.unused -= 1
            
    def resolveCollision(self, item, index):
        self.collisions += 1
        current = self.ls[index]
        while current.next != None:
            current = current.next
        current.next = DataItemEntry(item)
            

def main():
    length = 10000
    name_hashtable = HashTable(length)
    quote_hashtable = HashTable(length)
    items = []
    with open('MOCK_DATA.csv') as file:
        next(file) # Remove legend
        reader = csv.reader(file, )
        for line in reader:
            items.append(DataItem(line))
            
    name_start_time = time.time()
    for item in items:
        name_hashtable.add(item, item.movie_name)
    name_end_time = time.time()
    
    quote_start_time = time.time()
    for item in items:
        quote_hashtable.add(item, item.quote)
    quote_end_time = time.time()
        
    print("Statistics (djb2 Hash Function):")
    print("Movie Name Hash Table")
    print(f" Collisions: {name_hashtable.collisions}")
    print(f" Unused Buckets: {name_hashtable.unused}")
    print(f" Time Taken: {name_end_time-name_start_time}s")
    print("Quote Hash Table")
    print(f" Collisions: {quote_hashtable.collisions}")
    print(f" Unused Buckets: {quote_hashtable.unused}")
    print(f" Time Taken: {quote_end_time-quote_start_time}s")
        
if __name__ == '__main__':
    main()