import math
def end_corona(recovers, new_cases, active_cases):
      return(active_cases/new_cases)
  

soln=end_corona(4000, 2000, 77000)
print(round(soln))