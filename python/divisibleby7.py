# for number between given limits 
# find numbers divisible by 7 
# and not divisible by 5
start = 1000
end = 1200
op = ""
for x in range(1000, 1201):
    if (x%5!=0 and x%7 == 0):
        op = op + str(x) + ","
print op[0:len(op)-1]
    
