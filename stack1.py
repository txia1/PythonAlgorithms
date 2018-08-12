class Stack:
    def __init__(self):
        #initialize an empty list to start
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

#this function help determine if symbol balanced
#put "(" into stack, when encounter ")" pop out the "("inside the stack
#number of "(" must be same as ")"

# def parchecker(symbolString):
#     s=Stack()
#     balanced= True
#     index = 0
#
#     while index<len(symbolString) and balanced:
#         symbol = symbolString[index]
#         if symbol == "(":
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balanced = False
#             else:
#                 s.pop()
#         index = index + 1
#     if balanced and s.isEmpty():
#         return True
#     else:
#         return False
#
#
# print(parchecker('((()))'))
# print(parchecker('(()'))
#

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                # print(s.size())
                # print(s.peek())
                top = s.pop()
                #top = end of the closing,it needs to be one of the opening
                #symbol = first of the closing to match the end of opening
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))
