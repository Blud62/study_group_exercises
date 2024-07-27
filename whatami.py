#A ssume that obj already has a value of 42 when the code
# below starts running. Which of the subsequent statements
# reassign the variable? Which statements mutate the
# value of the object that obj references?
#  Which statements do neither?

obj = 42          # initialization

obj = 'ABcd'      # obj from 42 --> 'ABcd' hence, REASSIGNMENT
obj.upper()       # method is invoked on 'ABcd' --> 'ABCD' 
                  # but not returned/assigned hence, NEITHER
obj = obj.lower() # from 'ABCD' to new assignment --> 'abcd' hence REASSIGNMENT
print(len(obj))   #returns 4 --> Neither
obj = list(obj)   # takes 'abcd' turns it into a list --> ['a', 'b', 'c'. 'd'] REASSIGNMENT
obj.pop()         # pop last value off list --> ['a', 'b', 'c']  MUTATION
obj[2] = 'X'      # index 2 of list changed --> ['a', 'b', 'X']  MUTATION
obj.sort()        # list sorted --> ['X', 'a', 'b']  MUTATION
set(obj)          # Neither
obj = tuple(obj)  # assigns list to tuple --> ('X', 'a', 'b') REASSIGNMENT

print(obj)