n = int(input("Enter number of processes: "))

pid = []
at = [] # arrival time
bt = [] # burst time
rt = [] # remaining time
for i in range(n):
    pid.append(i+1)
    num1 = int(input("Enter Arrival Time of the Process: "))
    num2 = int(input("Enter Burst Time of the Process: "))
    at.append(num1)
    bt.append(num2)
    rt.append(num2) # remaining time is equal to burst time before round robin has started

t = 0
complete = 0
shortest = 0 # index of process with least remaining time
minimum = 100 # remaining time of process which has least remaining time

ct = [0]*n
ta = [0]*n
wt = [0]*n

# 1 iteration = 1s
while complete != n:
    
    # we are finding process with the least remaining time (storing its index in 'shortest')
    for i in range(n):
        if at[i] <= t and rt[i] < minimum and rt[i] > 0:
            minimum = rt[i]
            shortest = i

    rt[shortest] = rt[shortest] - 1
    minimum = rt[shortest]

    # when the process gets completed
    if minimum == 0:
        minimum = 100
        complete = complete + 1
        ct[shortest] = t + 1
        ta[shortest] = ct[shortest] - at[shortest]
        wt[shortest] = ta[shortest] - bt[shortest]

    # increment t by 1
    t = t + 1

    
print("pid \t at \t bt \t ct \t ta \t wt")
for i in range(n):
    print(pid[i],"\t",at[i],"\t",bt[i],"\t",ct[i],"\t",ta[i],"\t",wt[i])

avgwt = sum(wt)/n
avgta = sum(ta)/n

print("Average waiting time is",avgwt)
print("Average turnaround time is",avgta)





    
    
