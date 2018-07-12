
class stack:
    def __init__(self):
        #initialize an empty list to start
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return(self.items.pop())

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
#
# def transferbin(decimal):
#     s = stack()
#     result = ''
#     reminder = 0
#     num = 0
#     while decimal != 0:
#         reminder = decimal % 2
#         decimal = decimal // 2
#
#         s.push(reminder)
#
#     while not s.isEmpty():
#         result = result + str(s.pop())
#
#     return result
#
# print(transferbin(233))
#
def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(25,2))
print(baseConverter(25,16))
