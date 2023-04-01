n = int(input("Enter total number of processes: "))
bt = []
p = []
for i in range (n):
    num1 = int(input("Enter Burst time for the process: "))
    num2 = int(input("Enter Priority of the process: "))
    bt.append(num1)
    p.append(num2)

bt = [x for y, x in sorted(zip(p,bt))]
p.sort()

# completion time
ct = [] 
ct.append(bt[0])
for i in range(1,n):
    num = bt[i] + ct[i-1]
    ct.append(num)

# turn around time = completion time - arrival time
# since arrival time for all processes is 0, it will be the same as ct

# waiting time
wt = [0]
for i in range(1,n):
    num = ct[i-1]
    wt.append(num)

print("wt\tta\tbt\tp")
for i in range(n):
    print(wt[i],"\t",ct[i],"\t",bt[i],"\t",p[i])

avgwt = sum(wt)/n
avgta = sum(ct)/n

print("Average waiting time is",avgwt)
print("Average turnaround time is",avgta)






