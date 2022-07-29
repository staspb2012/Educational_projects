from operator import itemgetter

if __name__ == '__main__':
     students=[]
     lowest_score=0;
     for _ in range(int(input())):
         name = input()
         score = float(input())
         students.append([name, score])
     #get minimum value of nested list
     mn = min(students, key=itemgetter(1))[1]
     #remove minimum value from nested list
     filtered = [x for x in students if x[1] != mn]
     #get minimum value of nested list again (now it'll be second min as min. value has been already removed earlier)
     mn_fil = min(filtered,key=itemgetter(1))[1]
     #now print out the all second lowest values
     out = [x[0] for x in filtered if x[1] == mn_fil]
     out.sort()
     for x in out:
         print(x)