#my solution, n^2
def anagram(a1,b1):
    score = 0

    if len(a1) == len(b1):
        for i in range(len(list(a1))):
            for j in range(len(list(b1))):
                if a1[i] == b1[j]:
                    score = score + 1
                else:
                    break
                    # print('Not anagram!')
    if score == len(b1):
        print('Found it!')
    else:print('Not anagram!')


anagram('hello','oaleh')


#Example program,n^2
# def anagramSolution1(s1,s2):
#     if len(s1) != len(s2):
#         stillOK = False
#
#     alist = list(s2)
#
#     pos1 = 0 # initialize
#     stillOK = True #same length
#
#     while pos1 < len(s1) and stillOK:
#         pos2 = 0
#         found = False
#         while pos2 < len(alist) and not found: #alist = list(s2)
#             if s1[pos1] == alist[pos2]:
#                 found = True
#             else:
#                 pos2 = pos2 + 1
#
#         if found: #if found the match letter
#             alist[pos2] = None
#         else:
#             stillOK = False
#
#         pos1 = pos1 + 1
#
#     return stillOK
#
# print(anagramSolution1('hello','oaleh'))