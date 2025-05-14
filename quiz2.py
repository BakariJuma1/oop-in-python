numList=[4,7,10,32,33,11]

def checkEVen(numList):
    print('executing checkeven')
  
    # empty list to store the even and odd
    evenNum=[]
    oddNum=[]
    
    # function calculates he dividing by 2 to check if the number is odd and adds it to the empty list
    def calc(i):
        if numList[i]%2==0:
            evenNum.append(numList[i])
        else:
            oddNum.append(numList[i])
        
    # goes through  the numlist and calculates for every value    # 
    for i in range(len(numList)):
        calc(i)
    
    # returns the lists of even and odd
    def results():
        return(evenNum,oddNum) 
    return results  

numbers=checkEVen(numList)

even_numbers,odd_numbers=numbers()
print(f"even numbers:{even_numbers}")
print(f"odd numbers:{odd_numbers}")