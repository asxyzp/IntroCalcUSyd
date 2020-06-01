#Estimating Pi using the formula (n/2)tan(2*pi/n)
import math
import matplotlib.pyplot as plt

tanArr = []     #Stores of tan for incremental values of n 
errArr = []     #Stores error value of the formula with pi
numArr = []     #Stores counting/natural numbers till n
PiArr = []      #Stores pi in array for numArr.length values

for n in range(1000):
    if n>10:
        numArr.append(n)
        PiArr.append(math.pi)
        piVal = (n/2)*math.tan(2*math.pi/n)
        tanArr.append(piVal)
        errArr.append(piVal-math.pi)

plt.plot(numArr,PiArr,label="Pi = 3.14159...")
plt.legend()
plt.plot(numArr,tanArr,label="Pi approximation");
plt.legend()
plt.xlabel("x (Real numbers)")
plt.ylabel("y (Real numbers)")
plt.show()