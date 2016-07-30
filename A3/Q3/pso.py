#PARTICLE SWARM OPTIMIZATION WITH
#regular, inertia, Vmax, constrictionFactor
#with GlobalBest and NeighbourHoodBest using Ring topology
#using inertia from http://www.softcomputing.net/nabic11_7.pdf
#using constrictionFactor from https://svn-d1.mpi-inf.mpg.de/AG1/MultiCoreLab/papers/EbehartShi00%20-%20Inertia%20Weights%20and%20Construction%20Factors.pdf
#using topologies from https://svn-d1.mpi-inf.mpg.de/AG1/MultiCoreLab/papers/KennedyMendes02%20-%20Population%20Structure%20and%20PSO.pdf
#and https://www.researchgate.net/publication/221616406_A_Comparative_Study_of_Neighborhood_Topologies_for_Particle_Swarm_Optimizers
#procedure pseudo-code from http://www.swarmintelligence.org/tutorials.php

import random, numpy
xmax = 5
ymax = 5
xmaxVel = 7.5
ymaxVel = 7.5
localFactor = 2
globalFactor = 2.5
inertia = 0.7
successes = 0
failures = 0
convergenceFactor = 1
successFactor = 20
failureFactor = 10
bestParticle = None
#CONSTRICTION FACTOR
phi = globalFactor + localFactor
constrictionFactor = 2 / abs(2 - phi - (phi**2 - 4*phi)**(0.5))

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
        #print self.constrictionFactor
    def updateConstriction(self, globalBestPos):
        randomPersonal = random.random()
        randomGlobal = random.random()

        #CONSTRICTION FACTOR
        xVelocityPersonal = constrictionFactor*localFactor*randomPersonal*(self.personalBestPos[0]-self.position[0])
        xVelocityGlobal = constrictionFactor*globalFactor*randomGlobal*(globalBestPos[0]-self.position[0])
        yVelocityPersonal = constrictionFactor*localFactor*randomPersonal*(self.personalBestPos[1]-self.position[1])
        yVelocityGlobal = constrictionFactor*globalFactor*randomGlobal*(globalBestPos[1]-self.position[1])
        self.velocity = tuple(((self.position[0]*constrictionFactor+xVelocityPersonal+xVelocityGlobal),\
            (self.position[1]*constrictionFactor+yVelocityPersonal+yVelocityGlobal)))
        self.position = tuple((max(min(self.position[0] + self.velocity[0], xmax),-1*xmax),\
            max(min(self.position[1] + self.velocity[1], ymax),-1*ymax)))

    def updateVmax(self, globalBestPos):
        randomPersonal = random.random()
        randomGlobal = random.random()
        #VMAX
        xVelocityPersonal = localFactor*randomPersonal*(self.personalBestPos[0]-self.position[0])
        xVelocityGlobal = globalFactor*randomGlobal*(globalBestPos[0]-self.position[0])
        yVelocityPersonal = localFactor*randomPersonal*(self.personalBestPos[1]-self.position[1])
        yVelocityGlobal = globalFactor*randomGlobal*(globalBestPos[1]-self.position[1])

        self.velocity = tuple((min(xmaxVel,max(-xmaxVel,(self.position[0] + xVelocityPersonal + xVelocityGlobal))),\
            min(ymaxVel,max(-ymaxVel,self.position[1] + yVelocityPersonal + yVelocityGlobal))))
        self.position = tuple((max(min(self.position[0] + self.velocity[0], xmax),-1*xmax),\
            max(min(self.position[1] + self.velocity[1], ymax),-1*ymax)))

    def updateInertia(self, globalBestPos):
        randomPersonal = random.random()
        randomGlobal = random.random()
        #INERTIA
        xVelocityPersonal = localFactor*randomPersonal*(self.personalBestPos[0]-self.position[0])
        xVelocityGlobal = globalFactor*randomGlobal*(globalBestPos[0]-self.position[0])
        yVelocityPersonal = localFactor*randomPersonal*(self.personalBestPos[1]-self.position[1])
        yVelocityGlobal = globalFactor*randomGlobal*(globalBestPos[1]-self.position[1])

        self.velocity = tuple(((self.position[0]*inertia+xVelocityPersonal+xVelocityGlobal),\
            (self.position[1]*inertia+yVelocityPersonal+yVelocityGlobal)))
        self.position = tuple((max(min(self.position[0] + self.velocity[0], xmax),-1*xmax),\
            max(min(self.position[1] + self.velocity[1], ymax),-1*ymax)))

    def update(self, globalBestPos):
        randomPersonal = random.random()
        randomGlobal = random.random()
        #REGULAR
        xVelocityPersonal = localFactor*randomPersonal*(self.personalBestPos[0]-self.position[0])
        xVelocityGlobal = globalFactor*randomGlobal*(globalBestPos[0]-self.position[0])
        yVelocityPersonal = localFactor*randomPersonal*(self.personalBestPos[1]-self.position[1])
        yVelocityGlobal = globalFactor*randomGlobal*(globalBestPos[1]-self.position[1])

        self.velocity = tuple(((self.position[0] + xVelocityPersonal + xVelocityGlobal),\
            (self.position[1] + yVelocityPersonal + yVelocityGlobal)))
        self.position = tuple((max(min(self.position[0] + self.velocity[0], xmax),-1*xmax),\
         max(min(self.position[1] + self.velocity[1], ymax),-1*ymax)))

    def updateBest(self, globalBestPos, newConvergenceFactor):
        randomX = random.uniform(-1,1)
        randomY = random.uniform(-1,1)
        if successes > successFactor:
            newConvergenceFactor *= 2
        elif failures > failureFactor:
            newConvergenceFactor /= 2

        self.velocity = tuple((inertia*self.velocity[0] - self.position[0] + self.personalBestPos[0] + newConvergenceFactor*randomX,
         inertia*self.velocity[1] - self.position[1] + self.personalBestPos[1] + newConvergenceFactor*randomY))
        return newConvergenceFactor

iterations = 0
particle_list = []
globalBest = 0
globalBestPos = (0,0)
population = 150
#print(constrictionFactor)
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
            #GUARANTEED CONVERGENCE
            """if particle != bestParticle:
                failures = 0
                successes = 0
                bestParticle = particle
            else:
                if fitness < bestParticle.personalBest:
                    successes += 1
                else:
                    failures += 1"""
            globalBest = fitness
            globalBestPos = particle.position
            #print(particle.velocity)
    #UPDATE
    #NEIGHBOURHOOD BEST, EDGE VALUES
    """lastIndex = len(particle_list) - 1
    if particle_list[lastIndex].personalBest < particle_list[1].personalBest:
        particle_list[0].update(particle_list[lastIndex].personalBestPos)
    else:
        particle_list[0].update(particle_list[1].personalBestPos)
    if particle_list[lastIndex - 1].personalBest < particle_list[0].personalBest:
        particle_list[lastIndex].update(particle_list[lastIndex-1].personalBestPos)
    else:
        particle_list[lastIndex].update(particle_list[0].personalBestPos)
    for index in range(1, len(particle_list) - 1):
        if particle_list[index-1].personalBest < particle_list[index+1].personalBest:
            neighbourhoodBestPos = particle_list[index-1].personalBestPos
        else:
            neighbourhoodBestPos = particle_list[index+1].personalBestPos
        particle_list[index].update(neighbourhoodBestPos)"""
    #GUARANTEED CONVERGENCE
    for particle in particle_list:
        if particle==bestParticle:
            convergenceFactor = particle.updateBest(globalBestPos, convergenceFactor)
        else:
            particle.update(globalBestPos)
    #REGULAR
    #for particle in particle_list:
    #    particle.update(globalBestPos)
    iterations+=1
    if iterations%1000==0:
        print("iteration: " + str(iterations) + " globalBest: " + str(globalBestPos) + ", val: " + str(globalBest))

print("final, globalBest: " + str(globalBestPos) + ", val: " + str(globalBest))
