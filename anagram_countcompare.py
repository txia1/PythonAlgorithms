#my solution
def anagram(a1,b1):
    counter = list('abcdefghijklimopqrstuvwxyz')
    numcount1 = 0
    finalcount1 = []
    numcount2 = 0
    finalcount2 = []
    for i in counter:
        if i in list(a1):
            numcount1 = numcount1 + 1
            finalcount1.append(numcount1)
        if i in list(b1):
            numcount2 = numcount2 + 1
            finalcount2.append(numcount1)

    if finalcount1 == finalcount2:
        return True
    else:
        return False

print(anagram('ldso','djos'))

#Example program

def anagramSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

print(anagramSolution4('apple','pleap'))
