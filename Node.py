class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None # there is no next node,'ground' node

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newData):
        self.data = newData

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item) # generate a new node, put it into temp
        temp.setNext(self.head) # link the old node(used to be the head) to the temp value
        self.head = temp # this temp value become the new head

    def size(self): #keep rotating until the head is equal to None
        current = self.head
        count = 0
        while current!= None:
            current = current.getNext()
            count = count + 1
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else: # if not found, rotate to the next node
                previous = current
                current = current.getNext

        if previous == None: #if at the beginning of the list, remove the head
            self.head = current.getNext()
        else: #if inside the list, skip the node you want to remove, link to the next
            previous.setNext(current.getNext())

mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))