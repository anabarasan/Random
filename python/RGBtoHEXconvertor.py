# rgb to hex converter
# input  255-255-255
# output #FFFFFF

def toHex(dec):
    x = (dec % 16)
    digits = "0123456789ABCDEF"
    rest = dec / 16
    if (rest == 0):
        return digits[x]
    return toHex(rest) + digits[x]
    
def codelen(code):
	code = str(code)
	if len(code) < 2:
		return "0" + code
	else:
		return code
		
code = raw_input("Enter rgb code (r-g-b) : ")
r, g, b = code.split("-")
r = int(r)
g = int(g)
b = int(b)
if (r > 255 or g > 255 or b > 255):
    print "INVALID rgb code"
else:
    print "#" + codelen(toHex(r)) + codelen(toHex(g)) + codelen(toHex(b))


