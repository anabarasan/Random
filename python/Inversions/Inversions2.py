from time import ctime
inversions = []
def sort(ip):
    if len(ip) == 1:
        return ip, 0
    else:
        seperateat = len(ip)/2
        left, a = sort(ip[:seperateat])
        right, b = sort(ip[seperateat:])
        result, c = merge(left, right)
        return result, (a+b+c)
        
def merge(left, right):
    i = j = count = 0
    sortedlist = []
    while len(left) > i or len(right) > j:
        if len(left) > i and len(right) > j:
            if left[i] <= right[j]:
                sortedlist.append(left[i])
                i+=1
            elif right[j] < left[i]:
                sortedlist.append(right[j])
                if i<len(left):
                    count += len(left)-i
                j+=1
        elif len(left) > i:
            sortedlist.append(left[i])
            i+=1
        elif len(right) > j:
            sortedlist.append(right[j])
            j+=1
    return sortedlist, count
    
#print "%s : %s = %s" % (ctime(), "Total No of Inversions" , sort([6,5,3,1,8,7,2,4,9])[1])
#print "%s : %s = %s" % (ctime(), "Total No of Inversions" , sort([1,3,5,2,4,6])[1])
print "%s : %s" % (ctime(), "Preparing input list..")
iparr = []
f = open("IntegerArray.txt")
for line in f:
    iparr.append(int(line))
f.close()
print "%s : %s" % (ctime(), "Beginning Sort")
inversions = sort(iparr)
print "%s : %s" % (ctime(), "Finishing Sort")
print "%s : %s = %s" % (ctime(), "Total No of Inversions", inversions[1])
