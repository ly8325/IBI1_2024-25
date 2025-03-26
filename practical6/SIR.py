# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#define a variables called susceptible of Susceptible population
susceptible=9999
#define a variables called infected of infected population
infected=1
#define a variables called recovered of recovered population
recovered=0
#define a variables called N of total population
N=10000
#define beta and gamma
beta=0.3
gamma=0.05
#create three lists for plots
infectedlist=[1]
recoveredlist=[0]
susceptiblelist=[9999]
#loop over 1000 time points
for i in range(0,1000):
   #make sure infected>=0
   if infected>0 and susceptible>0:
      #caculate the number of infected people
      a=np.random.choice(range(2),susceptible,p=[(1-beta*(infected/N)),beta*(infected/N)]).sum()
      #caculate the number of recovered people
      b=np.random.choice(range(2),infected,p=[(1-gamma),gamma]).sum()
   else:
      b=0
      a=0
   #caculate the new population of infected people
   infected=infected-b+a
   #caculate the new population of recovered people
   recovered=recovered+b
   #caculate the new population of susceptible people
   susceptible=N-infected-recovered
   #record the infected, recovered and susceptible population at each time point
   infectedlist.append(infected)
   recoveredlist.append(recovered)
   susceptiblelist.append(susceptible)
xlabel=range(0,1001)
#create three plots
plt.plot(xlabel,infectedlist,color='blue',label="infected")
plt.plot(xlabel,recoveredlist,color='green',label="recovered")
plt.plot(xlabel,susceptiblelist,color='yellow',label="susceptible")
plt.xlabel("time")
plt.ylabel("population")
plt.title("SIR model")
plt.legend()
plt.show()