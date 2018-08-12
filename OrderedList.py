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

class Orderedlist():
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
            print(current)
            count = count + 1

    def search(self,items):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == items:
                found = True
            else:
                if current.getData() > items:
                    stop = True
                else:
                    found = False


        return found
