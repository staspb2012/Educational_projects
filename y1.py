Stud1_r=str('Failed')
Stud1_m=int(78)
Stud2_r=('Passed')
Stud2_m=int(82)
Stud3_r=str('Passed')
Stud3_m=int(97)
Stud4_r=str('Passed')
Stud4_m=int(86)
Stud5_r=str('Passed')
Stud5_m=int(67)
Stud6_r=str('Passed')
Stud6_m=int(75)
result = [Stud1_r,Stud2_r,Stud3_r,Stud4_r,Stud5_r,Stud6_r]
mark = [Stud1_m,Stud2_m,Stud3_m,Stud4_m,Stud5_m,Stud6_m]
mark.sort()
mark_s=mark
result.sort()
result_s=result

result_s2=result
'''name_res = 0
while number in a:
     a.remove('Failed')'''

index_feiled_r = []

for i in range(0, len(result)):
    if result[i] == 'Failed':
        index_feiled_r.append(i)

indexes_feiled = []

for i in range(0, len(result)):
    if result[i] == 'Failed':
        indexes_feiled.append(i)

indexes_passed = []

for i in range(0, len(result)):
    if result[i] == 'Passed':
        indexes_passed.append(i)
print(index_feiled_r)
print(indexes_feiled,indexes_passed)
if mark[max(index_feiled_r)] > mark_s[min(indexes_passed)]:
    print('Professor Gruble is inconsistent in marking for students')
else:
    print('Professor Gruble is consistent in marking for students,'
          'the range for passing the exam is higher '
          + str(mark_s[max(indexes_feiled)]+1)+' points to '+str(max(mark))+ ' points')







#mark = [Student1_mark,Student2_mark,Student3_mark,Student4_mark]
#result = [Student1_result,Student2_result,Student3_result,Student4_result]
#mark_and_result1 = dict(zip(mark, result))'''
#print('Professor Gruble is consistent in marking for students,the range for passing the exam is higher ' + str(mark_s))
#elif mark_s>=73 and result_s=='Feiled':

'''Student1_result=str(input('Enter result:'))
Student1_mark=int(input('Enter mark:'))
Student1={Student1_result:Student1_mark}
Student2_result=str(input('Enter result:'))
Student2_mark=int(input('Enter mark:'))
Student2={Student2_result:Student2_mark}
Student3_result=str(input('Enter result:'))
Student3_mark=int(input('Enter mark:'))
Student3={Student3_result:Student3_mark}
Student4_result=str(input('Enter result:'))
Student4_mark=int(input('Enter mark:'))'''