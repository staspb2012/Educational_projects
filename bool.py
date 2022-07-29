'''stop = input('Введите stop to stop: ')
import random

help_dict={}
while stop != 'stop':
    input_name = input('Введите имя: ')
    if input_name not in help_dict:
        input_mark = input(f'Введите оценку {input_name}: ')
        input_pass =  input(f'Введите прошел или не прошел студент {input_name}: ')
        help_dict[input_name] = [input_mark, input_pass]
    elif input_name in help_dict:
        input_mark = input(f'Введите оценку {input_name}: ')
        input_pass = input(f'Введите прошел или не прошел студент {input_name}: ')
        help_dict[input_name + str(random.randint(0,1000))] = [input_mark, input_pass]

    stop = input('Введите stop to stop')

print(help_dict)'''

class_gruble={'stas': ['84', 'Passed'], 'stas195': ['78', 'Passed'], 'kate': ['65', 'Failed'], 'stas386': ['90', 'Passed'], 'stas829': ['72', 'Failed']}

result_class = list(class_gruble.values())

res_class_passed = [e for e in result_class  if e[1]!='Failed']

res_class_failed = [e for e in result_class  if e[1]!='Passed']

min_passed = min([el[0] for el in res_class_passed])


indexes_feiled = []

for i in range(0, len(result_class )):
    if result_class [i][1] == 'Failed':
        indexes_feiled.append(i)

if result_class [max(indexes_feiled)][0] >= min_passed or result_class[min(indexes_feiled)][0] >= min_passed:
    print('Professor Gruble is inconsistent in marking for students')
else:
    print('Professor Gruble is consistent in marking for students,'
          'the range for passing the exam is higher '
          + str(int(max([el[0] for el in res_class_failed]))+1)+' points to '+str(min_passed)+ ' points')
