import random

def throwDice(m, k, R):
    R = random.Random(237)
    tup = []
    for dice in range(m):
        tup.append(random.randrange(1, k+1))
    return tuple(tup)
#main code 
def main(SEED=237):
    random.seed(237)
    dic = int(input('Enter the number of dice: '))
    while dic<=0:
        if dic<=0: print('\nThe number of dice must be at least 1')
        dic=int(input('Please enter the number of dice: \n'))
    sid=int(input('\nEnter the number of sides on each die: \n'))
    while sid<=1:
        if sid<=1: print('The number of sides on each die must be at least 2')
        sid=int(input('Please enter the number of sides on each die: '))
    freq=[0]*(dic*sid-dic+1)
    tri=int(input('\nEnter the number of trials to perform: \n'))
    while tri<=0:
        if tri<=0:print('The number of trials must be at least 1')
        tri=int(input('Please enter the number of trials to perform: '))
    for tri in range(tri):
        tup=throwDice(dic,sid,freq)
        total=sum(tup)
        freq[total-dic]+=1
    #print('{:>4}{:>15}{:>30}{:>30}'.format('Sum','Frequency','Relative Frequency','Experimental Probability'))
    print('{:>4}{:>15}{:>22}{:>30}'.format('Sum','Frequency','Relative Frequency','Experimental Probability'))
    print('-'*70)
    for i in range(len(freq)):
        #print('{:>4}{:>12}{:>25.5}{:>25.2f} %'.format(dic+i,freq[i],freq[i]/tri,freq[i]*100/tri))
        print('{:>4}{:>11}{:>18.5}{:>21.2f} %'.format(dic+i,freq[i],freq[i]/tri,freq[i]*100/tri))
#end main 
if __name__=='__main__':
    main(SEED=237)
#main(SEED=237)

#m= dic
#k= sid
#n= tri








