import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def get_user_data():
    D={}
    D2 = {}
    while True:
        student_name = input("Enter the student name: ")
        student_info = {}
        scores = []
        num_subjects = int(input("Enter the number of subjects: "))
        for i in range(num_subjects):
            key = input("Enter the subject: ")
            value = input ("Enter the mark: ")
            scores.append(value)
            student_info.update({key:value})
        more_students = input('Enter "no" to quit or else enter "yes": ')
        if student_name in D:
            print(student_name, " is already inserted")
        else:
            D2[student_name] = scores
            D[student_name] = student_info
            del student_info
            del scores
        if more_students.lower() == "no":
            return D,D2
students,student_data = get_user_data() 
print(students)
def average_marks(main):
    average_marks = {}
    for x in main:
        L = main[x]
        print(L)
        s = 0
        for marks in L:
            s+=int(marks)
        average_marks[x] = s/len(L)
    return average_marks
average_marks_student_data = average_marks(student_data)

def findMin_Max(D,startidx):
        minimum_value = D[startidx]
        maximum_value = D[startidx]
        index_min = startidx
        for a in range(startidx, len(D)):
            if float(D[a])<float(minimum_value):
                minimum_value = D[a]
                index_min = a
            if float(D[a])>float(maximum_value):
                maximum_value = a
            else:
                pass
        return minimum_value,maximum_value,index_min
def swapvalues(D,idx1,idx2):
    D[idx1],D[idx2] = D[idx2],D[idx1]
    return D
def sort_a_list(D):
    sort = {} 
    for x in D:
        Initial = D[x]
        for c in range(len(Initial)):
            minimum,maximum,idx = findMin_Max(Initial,c)
            Initial = swapvalues(Initial,c,idx)
        sort[x]=Initial
    return sort
sorted_list = sort_a_list(student_data)

for x in sorted_list:
    print('Student: ',x, ', got an average mark of: ',average_marks_student_data[x])
    print('Student: ',x, ', has an ordered list of: ',sorted_list[x])
    print('Student: ',x, ', has a minimum of: ',sorted_list[x][0])
    print('Student: ',x, ', has a maximum of: ',sorted_list[x][-1])

import pandas as pd
d_student_data = pd.DataFrame(student_data)
path = r"C:/Users/dell/Documents/DATA ANALYSIS/student_records.xlsx"
d_student_data.to_excel(path,index="False")