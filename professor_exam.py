# Импорт модуль рандом для генераци нумерации студентов
import random

# Команда для остановки или продолжения
# ввода данных по результатам экзамена
stop = input('Нажмите enter чтобы продолжить ввод,'
             'чтобы остановить введите stop: ')

# Заполнение данных(номер студента,оценка,результат)
# по сдаче экзамена профессору Грублу
class_gruble = {}
while stop != 'stop':
    input_name = input('Введите имя: ')
    if input_name not in class_gruble:
        input_mark = input(f'Введите оценку {input_name}: ')
        input_result = input(f'Введите сдали ли студент {input_name}: ')
        class_gruble[input_name] = [input_mark, input_result]
    elif input_name in class_gruble:
        input_mark = input(f'Введите оценку {input_name}: ')
        input_result = input(f'Введите сдали ли студент {input_name}: ')
        class_gruble[input_name + str(random.randint(0, 250))] \
            = [input_mark, input_result]

    stop = input('Нажмите enter чтобы продолжить ввод,'
                 'чтобы остановить введите stop: ')
print(class_gruble)

# Создаем список по значением словаря для оценки
# последовательности в оценивании студентов
result_class = list(class_gruble.values())

# Список данных для студентов, которые сдали екзамен
res_class_passed = [e for e in result_class if e[1] != 'Failed']

# Список денных для студентов, которые не сдали екзамен
res_class_failed = [e for e in result_class if e[1] != 'Passed']

# Минимальное значение сдачи экзамена при котором профессор
# должен быть последовательным в оценивани сдачи екзамена
min_passed = min([el[0] for el in res_class_passed])

# Получаем индексы значений для негативных результатов экзамена
# чтобы сравнить их с минимальное значение сдачи
indexes_feiled = []

for i in range(0, len(result_class)):
    if result_class[i][1] == 'Failed':
        indexes_feiled.append(i)

# За выше проведенными действиями
# узнаем был ли последовательным профессор Грубла
if result_class[max(indexes_feiled)][0] >= min_passed \
        or result_class[min(indexes_feiled)][0] >= min_passed:
    print('Professor Gruble is inconsistent in marking for students')
else:
    print('Professor Gruble is consistent in marking for students,'
          'the range for passing the exam is higher '
          + str(int(max([el[0] for el in res_class_failed])) + 1)
          + ' points to ' + str(min_passed) + ' points')

