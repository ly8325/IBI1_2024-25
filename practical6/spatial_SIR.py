# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt 
#define beta and gamma
beta=0.3
gamma=0.05
# make array of all susceptible population
population=np.zeros((100,100))
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1
#define a function to get the neighbors of infected people
def get_neighbors(i, j, connectivity=8):
    if connectivity == 8:
        neighbors = [(i-1, j),(i+1, j),(i, j-1),(i, j+1),(i-1, j-1),(i-1, j+1),(i+1, j-1), (i+1, j+1)]
    #check if neighbors in the plot
    neighbors = [(x, y) for x, y in neighbors if 0 <= x < population.shape[0] and 0 <= y < population.shape[1]]
    return neighbors
#loop over 100 time points
for m in range(0,100):
    new_population = population.copy()
    #find infected people
    infected=np.where(population==1)
    for i, j in zip(infected[0], infected[1]):
        neighbors = get_neighbors(i, j, connectivity=8)
    for x, y in neighbors:
        if population[x, y] == 0:
            if np.random.choice(range(2),1,p=[(1-beta),beta]).sum()==1:
                new_population[x, y] = 1      
    if population[i, j] == 1: 
        if np.random.choice(range(2),1,p=[(1-gamma),gamma]).sum()==1:
            new_population[i, j] = 2
    population = new_population
plt.figure(figsize=(6,4),dpi=150)
cmap = plt.cm.colors.ListedColormap(['purple', 'yellow', 'green'])
plt.imshow(population,cmap=cmap,interpolation='nearest')
plt.show()