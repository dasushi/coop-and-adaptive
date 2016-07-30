import random, numpy

def difference(particle1, particle2):
    return tuple(numpy.subtract(particle1.position, particle2.position))

def calculate_fitness(particle):
    return (4 - 2.1*(particle.positon[0]**2) + \
     (particle.positon[0]**4)/3)*(particle.positon[0]**2) + \
     particle.positon[0]*particle.positon[1] + \
     (-4 + 4*(particle.positon[1]**2))*(particle.positon[0]**2)

class swarmParticle:
    """A class for a particle in a swarm"""
    XMAX = 5
    YMAX = 5
    position = (0,0)
    velocity = (0,0)
    personalBest = 0
    personalBestPos = (0,0)
    factor1 = 2
    factor2 = 2.5
    def __init__(self):
        self.position = (random.uniform(-1*XMAX, XMAX), random.uniform(-1*YMAX, YMAX))
    def update(self, globalBestPos):
        self.velocity = tuple(numpy.add(numpy.multiply(
         factor1, random.random(), difference(personalBest, positon)),
         numpy.multiply(factor2, random.random(), difference(globalBestPos, positon))))
        self.position = tuple(numpy.add(position, velocity))

iterations = 0
particle_list = []
globalBest = 0
globalBestPos = (0,0)
population = 100
for particle in range(0, population):
    particle_list.append(swarmParticle())

while (iterations < 10,000):
    for particle in particle_list:
        fitness = calculate_fitness(particle, particle_list)
        if fitness < particle.personalBest:
            particle.personalBest = fitness
            particle.personalBestPos = particle.position
        if fitness < globalBest:
            globalBest = fitness
            globalBestPos = particle.position
    #UPDATE
    for particle in particle_list:
        particle.update(globalBestPos)
    iterations++
    if iterations%1000==0:
        print("globalBest: " + globalBestPos ", val: " + globalBest)
