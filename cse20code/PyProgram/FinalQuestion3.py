#FinalQuestion3 

def isPalindrome(s):
    # begin here 
    return s == s [::-1]
    
s = input("enter a word:")
answer = isPalindrome(s)
if answer: 
    print("True")
else: 
    print("False")

    