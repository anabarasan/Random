# nthdivisible
# find the highest n digit number divisible by n
# given input 2,5,7 output should be 98, 99995, 9999997

seed = "9"
input = raw_input()
ips = input.split(",")
op = ""
for ip in ips:
    startval = int(seed*int(ip))
    chk = True
    while chk:
        if (startval % int(ip)) == 0:
            op = op + str(startval) + ","
            chk = False
        startval = startval -1
print op[0:len(op)-1]

