

'''#Вводимо дані ,які проставив професор
Student1_result=str(input('Enter result:'))
Student1_mark=int(input('Enter mark:'))
Student1={Student1_result:Student1_mark}
Student2_result=str(input('Enter result:'))
Student2_mark=int(input('Enter mark:'))
Student2={Student2_result:Student2_mark}
Student3_result=str(input('Enter result:'))
Student3_mark=int(input('Enter mark:'))
Student3={Student3_result:Student3_mark}
Student4_result=str(input('Enter result:'))
Student4_mark=int(input('Enter mark:'))
Student5_result=str(input('Enter result:'))
Student5_mark=int(input('Enter mark:'))
Student6_result=str(input('Enter result:'))
Student6_mark=int(input('Enter mark:'))
mark  = [Student1_mark,Student2_mark,Student3_mark,Student4_mark,Student5_mark,Student6_mark]
result= [Student1_result,Student2_result,Student3_result,Student4_result,Student5_result,Student6_result]
mark_passed = [Student1_mark,Student2_mark,Student3_mark,Student4_mark,Student5_mark,Student6_mark]'''

#За даними професора створюємо списки результатів та оцінок
mark  = [84,78,65,90,72]
result= ['Passed','Passed','Passed','Passed','Failed']

#Дублємо спиоск оцінок для отримання межі для здачі екзему при умові, що професор був послідовний
mark_passed = [84,78,65,90,72]


#Отримуємо индекси результатів для студентів, які не здали екзамен
indexes_feiled = []

for i in range(0, len(result)):
    if result[i] == 'Failed':
        indexes_feiled.append(i)
print(indexes_feiled)
# Отримуємо индекси для оцінок ,які відповідають умові,що екзамен зданий
del_idx = {min(indexes_feiled),max(indexes_feiled)}
mark_passed[:] = [x for i,x in enumerate(mark_passed) if i not in del_idx]

#Сортуємо отримані індекси оцінок для отримання мінімальної під індексом [0]
mark_passed.sort()

if mark[max(indexes_feiled)] > mark[0] and mark[min(indexes_feiled)] > mark[0]:
    print('Professor Gruble is inconsistent in marking for students')
else:
    print('Professor Gruble is consistent in marking for students,'
          'the range for passing the exam is higher '
          + str(mark[max(indexes_feiled)]+1)+' points to '+str(max(mark))+ ' points')


