import numpy as np

allo = np.array([[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]])
max = np.array([[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]])
avl = np.array([3,3,2])
ans = np.array([0]*5)
finish = np.array([0]*5)
need = np.array([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]])

for i in range(5):
    need[i] = np.subtract(max[i],allo[i])

complete = 0
while complete != 5:
    for i in range(5):
        if np.less_equal(need[i][0],avl[0]) and np.less_equal(need[i][1],avl[1]) and np.less_equal(need[i][2],avl[2]) and finish[i]==0:
            avl = np.add(avl,allo[i])
            finish[i] = 1
            ans[complete] = i
            complete = complete + 1
            
print("Need matrix: ")
print(need)
print("Safe Sequence: ",ans)
