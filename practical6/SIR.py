# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#define a variables called susceptible of Susceptible population
susceptible=9999
#define a variables called injected of injected population
injected=1
#define a variables called recovered of recovered population
recovered=0
#define a variables called N of total population
N=10000
#define beta and gamma
beta=0.3
gamma=0.05
#create three lists for bar plots
injectedlist=[1]
recoveredlist=[0]
susceptiblelist=[9999]
#loop over 1000 time points
for i in range(0,1000):
     #think of a situation that nobody is injected
    if injected<=0:
       print("There is no people being infected")
       break
    #caculate the probability of injected people
    a=np.random.choice(range(2),1,p=[beta*(injected/N),(1-beta*(injected/N))])
    if a==0:
       injected=injected+1
    #caculate the probability of recovered people
    for n in range(0,injected):
        b=np.random.choice(range(2),1,p=[gamma,(1-gamma)])
        if b ==0:
           injected=injected-1
           recovered=recovered+1
    susceptible=N-injected
    #record the injected, recovered and susceptible population at each time point
    injectedlist.append(injected)
    recoveredlist.append(recovered)
    susceptiblelist.append(susceptible)
xlabel=range(0,len(injectedlist))
plt.plot(xlabel,injectedlist,marker='o',linestyle='-',color='b',label="injected")