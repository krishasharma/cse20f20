#Quiz5Question2 

def wordFreq(s):      
    s = s.split()          
    str2 = []
    for i in s:              
        if i not in str2: 
            str2.append(i)     
    for i in range(0, len(str2)): 
        print(str2[i], ':', s.count(str2[i]), ' ', end = '')  

def main(): 
    s ='one one two one two three one two three four'
    wordFreq(s)                    
  
if __name__=="__main__": 
    main()             # call main function