class Deque:
    def __init__(self):
        self.items = []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
# q = Deque()
#
# q.addFront("monkey")
# q.addRear('king')
# print(q.removeRear())
# print(q.isEmpty())
# print(q.size())

def Palindrome(wordcheck):
    q = Deque()

    for i in wordcheck:
        q.addRear(i)

    while q.size() > 1:
        if q.removeRear() != q.removeFront():
            return False

    return True
print(Palindrome('dsafdsf'))