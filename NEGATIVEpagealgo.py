def futureIndex(num,remPages):
    for i in range(len(remPages)):
        if num == remPages[i]:
            return i
    return len(remPages)

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 4
frame = pages[:4]

hit_count = 0
miss_count = 4

for i in range(4,len(pages)):
    if pages[i] in frame:
        hit_count = hit_count + 1
    else:
        miss_count = miss_count + 1
        index = 0
        biggest = 0 
        for j in range(4):
            dist = futureIndex(frame[j],pages[i:])
            if dist > biggest:
                biggest = dist
                index = j
        frame[index] = pages[i]

print("Page Hits:",hit_count)
print("Page Faults:",miss_count)

