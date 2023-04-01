n = int(input("Enter total number of processes: "))

bt = []
for i in range (n):
    num = int(input("Enter Burst Time for the Process: "))
    bt.append(num)

# FCFS
wt = [0]
for i in range(1,n):
    num = wt[i-1] + bt[i-1]
    wt.append(num)

ta = []
for i in range (n):
    num = wt[i] + bt[i]
    ta.append(num)

print("pid \t bt \t wt \t ta")
for i in range(n):
    print(i,"\t",bt[i],"\t",wt[i],"\t",ta[i])

print("Average Waiting Time with FCFS is",sum(wt)/n)
print("Average TurnAround Time with FCFS is",sum(ta)/n)

# SJF
bt.sort() # the only difference

wt = [0]
for i in range(1,n):
    num = wt[i-1] + bt[i-1]
    wt.append(num)

ta = []
for i in range (n):
    num = wt[i] + bt[i]
    ta.append(num)

print("pid \t bt \t wt \t ta")
for i in range(n):
    print(i,"\t",bt[i],"\t",wt[i],"\t",ta[i])

print("Average Waiting Time with SJF is",sum(wt)/n)
print("Average TurnAround Time with SJF is",sum(ta)/n)

