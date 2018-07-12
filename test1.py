import random
import string

def stgene(anystr):
    picklist =''
    strlist = 'abcdefghijklimopqrstuvwxyz '
    for i in range(anystr):
        picklist = picklist + strlist[random.randrange(27)]
    return picklist

def score(strinput,goal):
    numscore = 0
    for i in range(len(goal)):
        if strinput[i] == goal[i]:
            numscore = numscore + 1
    finalscore = numscore/len(strinput)
    return finalscore
# while True:
#     print(score(stgene(28),'methinks it is like a weasel'))

def main():
    goalstring = 'methinks it is like a weasel'
    newstring = stgene(28)
    best = 0
    newscore = score(goalstring,newstring)

    while newscore < 1:
        if newscore > best:
            print(newscore,newstring)
            best = newscore
        newstring = stgene(28)
        newscore = score(goalstring,newstring)

main()