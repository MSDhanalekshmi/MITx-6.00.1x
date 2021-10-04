def printMove(fr,to):
   print('Move from ' + str(fr) + ' to ' + str(to))


def Towers(n,fr,to,spare):
   if n == 1:
      printMove(fr,to)
   else:
      Towers(n-1,fr,spare,to)
      Towers(1,fr,to,spare)
      Towers(n-1,spare,to,fr)


print(Towers(4,'P1','P2','P3'))










# def h(n, start, end):
#     '''
#     Prints the list of steps required to move 
#     n disks from the start rod to the end rod 
#     >>>hanoi(2,1,3)
#     1 --> 2
#     1 --> 3
#     2 --> 3
#     '''
#     if n == 1:
#         pm(start, end)
#     else:
#         other = 6 - (start + end)
#         h(n-1, start, other)
#         pm(start, end)
#         h(n-1, other, end)
#         return ""


# def pm(start, end):
#     '''
#     prints a move in the correct format
#     >>>pm(1,3)
#     1 ---> 3
#     '''

#     print(start, "-->", end)
#     return ""


# print(h(3, 1, 3))
