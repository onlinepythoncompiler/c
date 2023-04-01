n = int(input("Enter number of processes: "))

pid = []
bt = [] # burst time
rt = [] # remaining time
for i in range(n):
    num1 = int(input("Enter ID of the process: "))
    num2 = int(input("Enter Burst Time of the process: "))
    pid.append(num1)
    bt.append(num2)
    rt.append(num2) # remaining time is equal to burst time before round robin has started
print(bt)

q = int(input("Enter quantum time: "))
t = 0
complete = 0

ct = [0]*n # completion time
wt = [0]*n # waiting time

while complete != n:
    for i in range(n):
        if rt[i] > 0:
            if rt[i] > q:
                t = t + q
                rt[i] = rt[i] - q
            else:
                t = t + rt[i]
                rt[i] = 0
                ct[i] = t
                wt[i] = ct[i] - bt[i]
                complete = complete + 1

print("pid \t bt \t rt \t ct \t wt")
for i in range(n):
    print(pid[i],"\t",bt[i],"\t",rt[i],"\t",ct[i],"\t",wt[i])

avgwt = sum(wt)/n
avgta = sum(ct)/n

print("Average waiting time is",avgwt)
print("Average turnaround time is",avgta)
                
                
