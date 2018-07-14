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