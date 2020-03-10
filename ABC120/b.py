a,b,k = map(int,input().split())
class stack:
    def __init__(self):
       self.items = []
        
    def is_empty(self):
       return self.items == []
        
    def push(self, item):
       self.items.append(item)
        
    def pop(self):
       return self.items.pop()
        
    def peek(self):
       return self.items[len(self.items)-1]
        
    def size(self):
       return len(self.items)

ansstack = stack()
for i in range(1, max(a, b) + 1):
    if a % i == 0 and b % i == 0:
        ansstack.push(i)
ans = 0
for i in range(k):
    ans = ansstack.pop()
print(ans)
