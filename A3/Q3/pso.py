import random, numpy
xmax = 5
ymax = 5
factor1 = 2
factor2 = 2.5

def difference(position1, position2):
    return tuple(numpy.subtract(position1, position2))

def calculate_fitness(particle):
    return ((4*particle.position[0]**2 - 2.1*(particle.position[0]**4) + \
     (particle.position[0]**6)/3) + \
     particle.position[0]*particle.position[1] + \
     ((particle.position[1]**4 - particle.position[1]**2))*4)

class swarmParticle:
    """A class for a particle in a swarm"""
    position = (0,0)
    velocity = (0,0)
    personalBest = 0
    personalBestPos = (0,0)
    def __init__(self):
        self.position = tuple((random.uniform(-1*xmax, xmax), random.uniform(-1*ymax, ymax)))
    def update(self, globalBestPos):
        randomPersonal = random.random()
        randomGlobal = random.random()
        self.velocity = tuple(numpy.add(numpy.add(self.velocity,
         tuple((factor1*randomPersonal*(self.personalBestPos[0]-self.position[0]),\
         factor1*randomPersonal*(self.personalBestPos[1]-self.position[1])))),\
         tuple((factor2*randomGlobal*(globalBestPos[0]-self.position[0]),\
         factor2*randomGlobal*(globalBestPos[1]-self.position[1])))))
        self.position = tuple((max(min(self.position[0] + self.velocity[0], xmax),-1*xmax),\
         max(min(self.position[1] + self.velocity[1], ymax),-1*ymax)))

iterations = 0
particle_list = []
globalBest = 0
globalBestPos = (0,0)
population = 150
for particle in range(0, population):
    particle_list.append(swarmParticle())

while iterations < 10000:
    #EVALUTATE FITNESS
    for particle in particle_list:
        fitness = calculate_fitness(particle)
        #COMPARE AND UPDATE BEST RESULTS
        if fitness < particle.personalBest:
            particle.personalBest = fitness
            particle.personalBestPos = particle.position
        if fitness < globalBest:
            globalBest = fitness
            globalBestPos = particle.position
    #UPDATE
    for particle in particle_list:
        particle.update(globalBestPos)
    iterations+=1
    if iterations%1000==0:
        print("iteration: " + str(iterations) + " globalBest: " + str(globalBestPos) + ", val: " + str(globalBest))
