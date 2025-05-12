def checkOddEven(x):
    if(x%2==0):
       return True
    else:
        return False
    
# print(checkOddEven(11))    


class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if (((a>=0 and b >0) or (a<0 and b>=0) and flag==False) or ((a<0 and b<0) and flag==True)):
            return True
        else:
            return False

sol=Solution()       
print(sol.checkStatus(1,-8,flag=False) )