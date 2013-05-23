# fibnocci

sequence_number = 10

a = 0
b = 1
c = 1

#print "#{a}\n"
puts a

while (c < sequence_number)
    d = a + b
    a = b
    b = d
    #print "#{d}\n"
    puts d
    c = c+1 
end
