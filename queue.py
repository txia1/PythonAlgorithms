import random

class queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        return self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items

# q = queue()
#
# q.enquue(4)
# q.enquue('dog')
# print(q.peek())
# q.dequeue()
# print(q.peek())

# def hotPotato(namelist, num):
#     simqueue = queue()
#     for name in namelist:
#         simqueue.enqueue(name)
#
#     while simqueue.size() > 1:
#         for i in range(num):
#             simqueue.enqueue(simqueue.dequeue())
#
#         simqueue.dequeue()
#
#     return simqueue.dequeue()
#
# print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

class Printer:
    def __init__(self,ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None: #if there is a task
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None: #if have task, is busy
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate
        #cancel out m in ppm? only page left?

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self,currenttime):
        return currenttime - self.timestamp

def simulation(numSeconds,pagesPerMinute):
    #numSeconds is a random number

    labprinter = Printer(pagesPerMinute)
    printQueue = queue()
    waitingtimes = []

    for currentSecond in range(numSeconds): #looping through every second
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        #push task to the queue

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
        # if printer is not busy and queue is not full

            nexttask = printQueue.dequeue() #dequeue the waiting list
            waitingtimes.append(nexttask.waitTime(currentSecond))
            #currenttime - self.timestamp(starting time) = waiting time

            labprinter.startNext(nexttask) #calculate the time to finish

        labprinter.tick() #tick time, deduct remaining time by 1 sec

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))

def newPrintTask():
    num = random.randrange(1,181) # the possibility of 1 task is per 180s
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)

