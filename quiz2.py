numList=[4,7,10,32,33,11]

def checkEVen(numList):
    print('executing checkeven')
    print(numList)

    evenNum=[]
    oddNum=[]

    def calc(i):
        if numList[i]%2==0:
            evenNum.append(numList[i])
        else:
            oddNum.append(numList[i])
        
    for i in range(len(numList)):
        calc(i)

    def results():
        return(evenNum,oddNum) 
    return results  

numbers=checkEVen(numList)

even_numbers,odd_numbers=numbers()
print(f"even numbers:{even_numbers}")
print(f"odd numbers:{odd_numbers}")