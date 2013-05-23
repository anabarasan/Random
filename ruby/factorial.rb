# factorial

factor = 10
factorial = 1
i = 1
while i <= factor
    factorial = factorial * i
    i = i + 1
end
puts factorial

def factorial(x)
    if x==1
        return 1
    else
        return x * factorial(x-1)  
    end
end

puts factorial(10)
