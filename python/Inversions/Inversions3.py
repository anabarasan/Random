from time import ctime
count = 0

def sort(ip):
    if len(ip) == 1:
        return ip
    else:
        seperateat = len(ip)/2
        left =ip[:seperateat]
        right = ip[seperateat:]
        return merge(sort(left), sort(right))
        
def merge(left, right):
    i = j = 0
    sortedlist = []
    global count
    while len(left) > i or len(right) > j:
        if len(left) > i and len(right) > j:
            #print left, right
            if left[i] <= right[j]:
                sortedlist.append(left[i])
                i+=1
            elif right[j] < left[i]:
                sortedlist.append(right[j])
                if i<len(left):
                    count += len(left) - i
                j+=1
        elif len(left) > i:
            sortedlist.append(left[i])
            i+=1
        elif len(right) > j:
            sortedlist.append(right[j])
            j+=1
    return sortedlist
    

print "%s : %s" % (ctime(), "Preparing input list..")
iparr = []
f = open("IntegerArray.txt")
for line in f:
    iparr.append(int(line))
f.close()
print "%s : %s" % (ctime(), "Beginning Sort")
sort(iparr)
#print sort([6,5,3,1,8,7,2,4,9])
#print sort([1,3,5,2,4,6])
print "%s : %s" % (ctime(), "Finishing Sort")
print "%s : %s = %s" % (ctime(), "Total No of Inversions" , count)

