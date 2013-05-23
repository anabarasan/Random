import sys

if len(sys.argv) > 1:
    sample = sys.argv[1]
else:
    sample= raw_input("Enter the text to be tested for palindrome ")
    
def Palindrome(word):
    reversedword = word[::-1]
    if (sample == reversedsample):
        print "Palindrome"
    else:
        print "Not Palindrome"
        
palindrome("malayalam")
palindrome("palindrome")
