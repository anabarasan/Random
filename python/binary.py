# binarymath
# from the given comma seperated input of binary numbers
# find those which are divisible by 3
# input  : 10,11,110,1001
# output : 11,110,1001

inpu = raw_input()
ips = inpu.split(",")
op = ""
for ip in ips:
    opr1 = int(ip,2)
    opr2 = 3
    if ((opr1 % opr2) == 0):
        op = op + ip + ","
print op[0:len(op)-1]
