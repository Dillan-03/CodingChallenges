python = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    temp = []
    temp.append(name)
    temp.append(score)
    python.append(temp) #2d array

python.sort(key=lambda x:x[1])
x = python[0][1]

ans = []
final_ans = []
for i in python:
    if i[1] != x:
        ans.append(i)
    


two = ans[0][1]
for i in ans:
    
    if i[1] == two:
        final_ans.append(i)

output = [] 
for student in final_ans:
    output.append(student[0])

output.sort()
for each in output:
    print(each) 