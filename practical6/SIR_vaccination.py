# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#create a SIR model of 0 get vaccinated
susceptible=9999
infected=1
recovered=0
N=10000
beta=0.3
gamma=0.05
infectedlist0=[1]
for i in range(0,1000):
   if infected>0 and susceptible>0:
      a=np.random.choice(range(2),susceptible,p=[(1-beta*(infected/N)),beta*(infected/N)]).sum()
      b=np.random.choice(range(2),infected,p=[(1-gamma),gamma]).sum()
   else:
      b=0
      a=0
   infected=infected-b+a
   recovered=recovered+b
   susceptible=N-infected-recovered
   infectedlist0.append(infected)
xlabel=range(0,1001)
#create a SIR model of ten percent get vaccinated
susceptible=8999
infected=1
recovered=1000
N=10000
beta=0.3
gamma=0.05
infectedlist10=[1]
for i in range(0,1000):
   if infected>0 and susceptible>0:
      a=np.random.choice(range(2),susceptible,p=[(1-beta*(infected/N)),beta*(infected/N)]).sum()
      b=np.random.choice(range(2),infected,p=[(1-gamma),gamma]).sum()
   else:
      b=0
      a=0
   infected=infected-b+a
   recovered=recovered+b
   susceptible=N-infected-recovered
   infectedlist10.append(infected)
#create a SIR model of 20 percent get vaccinated
susceptible=7999
infected=1
recovered=2000
N=10000
beta=0.3
gamma=0.05
infectedlist20=[1]
for i in range(0,1000):
   if infected>0 and susceptible>0:
      a=np.random.choice(range(2),susceptible,p=[(1-beta*(infected/N)),beta*(infected/N)]).sum()
      b=np.random.choice(range(2),infected,p=[(1-gamma),gamma]).sum()
   else:
      b=0
      a=0
   infected=infected-b+a
   recovered=recovered+b
   susceptible=N-infected-recovered
   infectedlist20.append(infected)
#create a SIR model of 30 percent get vaccinated
susceptible=6999
infected=1
recovered=3000
N=10000
beta=0.3
gamma=0.05
infectedlist30=[1]
for i in range(0,1000):
   if infected>0 and susceptible>0:
      a=np.random.choice(range(2),susceptible,p=[(1-beta*(infected/N)),beta*(infected/N)]).sum()
      b=np.random.choice(range(2),infected,p=[(1-gamma),gamma]).sum()
   else:
      b=0
      a=0
   infected=infected-b+a
   recovered=recovered+b
   susceptible=N-infected-recovered
   infectedlist30.append(infected)
#create a SIR model of 40 percent get vaccinated
susceptible=5999
infected=1
recovered=4000
N=10000
beta=0.3
gamma=0.05
infectedlist40=[1]
for i in range(0,1000):
   if infected>0 and susceptible>0:
      a=np.random.choice(range(2),susceptible,p=[(1-beta*(infected/N)),beta*(infected/N)]).sum()
      b=np.random.choice(range(2),infected,p=[(1-gamma),gamma]).sum()
   else:
      b=0
      a=0
   infected=infected-b+a
   recovered=recovered+b
   susceptible=N-infected-recovered
   infectedlist40.append(infected)
#create a SIR model of 50 percent get vaccinated
susceptible=4999
infected=1
recovered=5000
N=10000
beta=0.3
gamma=0.05
infectedlist50=[1]
for i in range(0,1000):
   if infected>0 and susceptible>0:
      a=np.random.choice(range(2),susceptible,p=[(1-beta*(infected/N)),beta*(infected/N)]).sum()
      b=np.random.choice(range(2),infected,p=[(1-gamma),gamma]).sum()
   else:
      b=0
      a=0
   infected=infected-b+a
   recovered=recovered+b
   susceptible=N-infected-recovered
   infectedlist50.append(infected)
#create a SIR model of 60 percent get vaccinated
susceptible=3999
infected=1
recovered=6000
N=10000
beta=0.3
gamma=0.05
infectedlist60=[1]
for i in range(0,1000):
   if infected>0 and susceptible>0:
      a=np.random.choice(range(2),susceptible,p=[(1-beta*(infected/N)),beta*(infected/N)]).sum()
      b=np.random.choice(range(2),infected,p=[(1-gamma),gamma]).sum()
   else:
      b=0
      a=0
   infected=infected-b+a
   recovered=recovered+b
   susceptible=N-infected-recovered
   infectedlist60.append(infected)
   #create a SIR model of 70 percent get vaccinated
susceptible=2999
infected=1
recovered=7000
N=10000
beta=0.3
gamma=0.05
infectedlist70=[1]
for i in range(0,1000):
   if infected>0 and susceptible>0:
      a=np.random.choice(range(2),susceptible,p=[(1-beta*(infected/N)),beta*(infected/N)]).sum()
      b=np.random.choice(range(2),infected,p=[(1-gamma),gamma]).sum()
   else:
      b=0
      a=0
   infected=infected-b+a
   recovered=recovered+b
   susceptible=N-infected-recovered
   infectedlist70.append(infected)
#create a SIR model of 80 percent get vaccinated
susceptible=1999
infected=1
recovered=8000
N=10000
beta=0.3
gamma=0.05
infectedlist80=[1]
for i in range(0,1000):
   if infected>0 and susceptible>0:
      a=np.random.choice(range(2),susceptible,p=[(1-beta*(infected/N)),beta*(infected/N)]).sum()
      b=np.random.choice(range(2),infected,p=[(1-gamma),gamma]).sum()
   else:
      b=0
      a=0
   infected=infected-b+a
   recovered=recovered+b
   susceptible=N-infected-recovered
   infectedlist80.append(infected)
#create a SIR model of 90 percent get vaccinated
susceptible=999
infected=1
recovered=9000
N=10000
beta=0.3
gamma=0.05
infectedlist90=[1]
for i in range(0,1000):
   if infected>0 and susceptible>0:
      a=np.random.choice(range(2),susceptible,p=[(1-beta*(infected/N)),beta*(infected/N)]).sum()
      b=np.random.choice(range(2),infected,p=[(1-gamma),gamma]).sum()
   else:
      b=0
      a=0
   infected=infected-b+a
   recovered=recovered+b
   susceptible=N-infected-recovered
   infectedlist90.append(infected)
#create a SIR model of 100 percent get vaccinated
susceptible=0
infected=0
recovered=10000
N=10000
beta=0.3
gamma=0.05
infectedlist100=[0]
for i in range(0,1000):
   if infected>0 and susceptible>0:
      a=np.random.choice(range(2),susceptible,p=[(1-beta*(infected/N)),beta*(infected/N)]).sum()
      b=np.random.choice(range(2),infected,p=[(1-gamma),gamma]).sum()
   else:
      b=0
      a=0
   infected=infected-b+a
   recovered=recovered+b
   susceptible=N-infected-recovered
   infectedlist100.append(infected)
xlabel=range(0,1001)
#create three plots
plt.plot(xlabel,infectedlist0,color='blue',label="0")
plt.plot(xlabel,infectedlist10,color='green',label="10%")
plt.plot(xlabel,infectedlist20,color='black',label="20%")
plt.plot(xlabel,infectedlist30,color='pink',label="30%")
plt.plot(xlabel,infectedlist40,color='purple',label="40%")
plt.plot(xlabel,infectedlist50,color='red',label="50%")
plt.plot(xlabel,infectedlist60,color='brown',label="60%")
plt.plot(xlabel,infectedlist70,color='gray',label="70%")
plt.plot(xlabel,infectedlist80,color='orange',label="80%")
plt.plot(xlabel,infectedlist90,color='yellow',label="90%")
plt.plot(xlabel,infectedlist100,color='darkblue',label="100%")
plt.xlabel("time")
plt.ylabel("infected population")
plt.title("SIR model with different vaccination rates")
plt.legend()
plt.show()