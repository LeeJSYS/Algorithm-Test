import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
array=[]
for i in range(n):
    name, *score= input().split()
    array.append([str(name), *map(int, score)])

array.sort(key = lambda student_s: (-student_s[1],student_s[2],-student_s[3],student_s[0]))

for i in range(n):
    print(array[i][0])
