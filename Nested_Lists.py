if __name__ == '__main__':
    students=[]      #Creating a list for storing Students with their marks
    for _ in range(int(input())):
        name = input()            #taking names of student
        score = float(input())    #take score of each student
        students.append((name,score))      #appending the name and score of students one by one
    second_lowest=sorted(list(set([x[1] for x in students])))[1]            #A
    second_students=sorted([s for s,g in students if g==second_lowest])     #B
    for s in second_students:       #For printing the second student
        print(s)


#Step by step explaination of A and # B

# A  :  second_lowest=sorted(list(set([x[1] for x in students])))[1]
# [x[1] for x in students] - In this the x[1] is accesinh the score element from the student list
# set  -  Set is used to remove duplicate and during this process list is converted into Set
# List  - It helps to remove set into List
# Sorting - It sort the element in accesing order
# the outer [1] - As we need to acess the second lowest score and taht is present in 1st position so we wrote [1]

# B :  second_students=sorted([s for s,g in students if g==second_lowest])
# s ==> student,  g==> score
# s for s,g in students - this line let us select the name in the tuples. So you select s for s,g ==> you select name for name,score
# if g == second_lowest - this line select only the name that their score are equal to the second lowest. if g == second_lowest ==> if score match the second lowest score.
# The method (sorted) sorts the name in alphabetical order.
