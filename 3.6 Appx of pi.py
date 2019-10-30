a = int(input("Enter the number of iterations:")
import pi from math
i = 0;
c_i = 1;
p_i = pi/4 == 1 - 1/3 + 1/5 - 1/7 + ... 
for i in range(1, a+1):
        

print("The approximation of pi is",a)
        
        
Iterations = int(input("Enter the number of iterations : "));
from math import pi
i = 0;
current_iteration = 1;
for i in range(1,Iterations+1):
    if(i % 2 != 0):
        i = pi/4 + 1 /current_iteration;
    else:
        i = pi/4 - 1 /current_iteration;
    current_iteration = current_iteration + 2;
appi = pi/4*4;
print("The approximation of pi is",appi)
