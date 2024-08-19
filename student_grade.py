import sys
sys.path.append('C:/Users/dell/Documents/DATA_ANALYSIS/')
#GET THE INFORMATION
def get_user_data():
    D={}
    while True:
        student_name = input("Enter the student name: ")
        marks_list = input("Enter the marks and separate with a comma: ")
        more_students = input('Enter "no" to quit or else enter "yes: ')
        if student_name in D:
            print(student_name, " is already inserted")
        else:
            D[student_name] = marks_list.split(",")
        if more_students.lower() == "no":
            return D
student_data = get_user_data() 
print(student_data)

#FIND THE AVERAGE
def average_marks(D):
    average_marks = {}
    for x in D:
        L = D[x]
        s = 0
        for marks in L:
            s+=int(marks)
        average_marks[x] = s/len(L)
    return average_marks
average_marks_student_data = average_marks(student_data)
for x in average_marks_student_data:
    print('Student: ',x, ', got an average mark of: ',average_marks_student_data[x])
    
#FIND MINIMUM AND MAXIMUM, THEN SORT IN ASCENDING ORDER
'''def findMin_Max(L):
    minimum_value = L[0]
    maximum_value = L[0]
    for a in L:
            if int(a)<int(minimum_value):
                minimum_value = a
            if int(a)>int(maximum_value):
                maximum_value = a
            else:
                pass
    return minimum_value,maximum_value
List = []
Din = [3,4,6,2,7,2,4]
for x in range(0,len(Din)):
    minimum,maximum = findMin_Max(Din)
    #print(type(minimum))
    List.append(minimum)
    #print(type(Din))
    Din.remove(minimum)
print(List)'''
'''def findMin_Max(D):
    min = {}
    idx = {}
   # max = {}
    for x in D:
        L = D[x]
        startidx = 0
        minimum_value = L[startidx]
        #idx = startidx
       # maximum_value = L[startidx]
        for a in L:
            if float(a)<float(minimum_value):
                minimum_value = a
                index_min = L.index(minimum_value)
                #print(index_min)
                #print(a)
            #elif int(a)>float(maximum_value):
              #  maximum_value = a
            else:
                pass
        min[x] = minimum_value
        idx[x] = index_min
        #max[x] = maximum_value
    return min,idx
print(findMin_Max(student_data))'''
import pandas as pd
d_student_data = pd.DataFrame(student_data)
path = r"C:/Users/dell/Documents/DATA ANALYSIS/student_records.xlsx"
d_student_data.to_excel(path,index="False")