# fibnocci

def fibnocci(x):
    a = 0
    b = 1
    c = 1
    print a
    while (c < x):
        d = a + b
        a = b
        b = d
        print d
        c = c+1

def fibnocci1(x):
    a = 0
    b = 1
    c = 1
    print a
    for c in range(1, x):
        d = a + b
        a = b
        b = d
        print d
        
fibnocci(10)
fibnocci1(10)
