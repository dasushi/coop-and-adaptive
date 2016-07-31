# -*- coding: utf-8 -*-
#Control systems with Genetic Algorithms
import control, random, matplotlib.pyplot as plt

alpha = 0.9
mutateRate = 0.25
crossoverRate = 0.6
kMin = 2
kMax = 18
tiMin = 1.05
tiMax = 9.42
tdMin = 0.26
tdMax = 2.37
size = 50
finalGeneration = 150
pc = 0.6
pm = 0.25

# Evalutate fitness of a solution
def fitness(Kp, ti, td):
    step = control.step(control.feedback(control.series(control.tf([ti*td, ti, 1],\
        [ti, 0]), control.tf(1, [1,6,11,6,0])), 1))

    stepVals = step[0]
    t = step[-1]
    overshoot = (stepVals.max()/stepVals[-1]-1)*100

    error = 0 # for ISE
    for val in step[0]:
        error += (val - 1)**2

    rise = 0
    settle = 0


    length = len(stepVals)
    for x in range(0, length-1):
        if stepVals[x] > stepVals[-1]*alpha:
            rise = t[x] - t[0]

    for x in range(2, length-1):
        if tiMin < abs(stepVals[-x]/stepVals[-1]):
            settle = t[length-x] - t[0]

    return 100000/(overshoot + rise + settle + (error**2)*10)

# Generate initial population set
def generate_initial_set(size):
    temp_list = []
    result_list = []
    found = 0
    while found < size:
        k = round(random.uniform(kMin, kMax), 2)
        ti = round(random.uniform(tiMin, tiMax), 2)
        td = round(random.uniform(tdMin, tdMax), 2)

        if [k, ti, td] not in temp_list: # check if result already exists
            found += 1
            temp_list.append([k, ti, td])
            fitnessValue = fitness(k, ti, td)
            result_list.append({[k, ti, td], round(fitnessValue, 3)})

    return result_list


def check_limits(k, ti, td):
    return [min(kMax,max(kMin, k)), min(tiMax,max(tiMin,ti)), min(tdMax,max(tdMin,td))]

def crossover(lst):
    final = []

    for i in range(0, len(lst) - 1, 2):
        mom = lst[i]
        dad = lst[i+1]
        #only crossover randomly, with arithmetic crossover
        if random.random() < crossoverRate:
            #child 1
            K1 = alpha*mom[0][0] + (1-alpha)*dad[0][0]
            Ti1 = alpha*mom[0][1] + (1-alpha)*dad[0][1]
            Td1 = alpha*mom[0][2] + (1-alpha)*dad[0][2]
            final.append({check_limits(K1, Ti1, Td1), round(fitnessFunction(K1, Ti1, Td1), 3)})

            #child 2
            K2 = alpha*dad[0][0] + (1-alpha)*mom[0][0]
            Ti2 = alpha*dad[0][1] + (1-alpha)*mom[0][1]
            Td2 = alpha*dad[0][2] + (1-alpha)*mom[0][2]
            final.append({check_limits(K2, Ti2, Td2), round(fitnessFunction(K2, Ti2, Td2), 3)})
        else:
            final.append(mom)
            final.append(dad)
    return final


def mutateValues(lst):
    results = []

    for item in lst:
        if random.random() < mutateRate:
            mutVal = random.random()
            k = kMin + mutVal*(kMax - kMin)
            ti = tiMin + mutVal*(tiMin - tiMin)
            td = tdMin + mutVal*(tdMax - tdMin)
            results.append({[k, ti, td], round(fitnessFunction(k, ti, td), 3)})
        else:
            results.append(lst[i])

    return results


def genetic_algorithm(initialPop, finalGeneration):
    fits = []
    generation = 0
    currentPop = sorted(initialPop, key= lambda x: x[1])
    while generation < finalGeneration:
        fitSum = sum([x[1] for x in currentPop])
        averageProb = (sum([x[1]/fitSum for x in currentPop]))/len(currentPop)
        parentPop = []

        for sol in currentPop:
            prob = sol[1]/fitSum
            expectedCount = prob/averageProb
            actualCount = int(round(expectedCount))

            for i in range(actualCount):
                parentPop.append(sol)

        random.shuffle(parentPop)
        crossPop = crossover(parentPop)

        random.shuffle(crossPop)
        mutatePop = sorted(mutateValues(crossPop), key= lambda x: x[1])

        currentPop[0] = mutatePop[-1]
        currentPop[1] = mutatePop[-2]

        currentPop = sorted(currentPop, key= lambda x: x[1])
        generation += 1

        fits.append(currentPop[-1][1])


    plt.plot(fits)
    return currentPop[-1]

found = 0
temp_list = []
result_list = []
while found < size: #populate list to desired size
    k = round(random.uniform(kMin, kMax), 2) #round to desired precision
    ti = round(random.uniform(tiMin, tiMax), 2)
    td = round(random.uniform(tdMin, tdMax), 2)

    if [k, ti, td] not in temp_list: # check if result already exists
        found += 1
        temp_list.append([k, ti, td])
        fitnessValue = fitness(k, ti, td)
        result_list.append({[k, ti, td], round(fitnessValue, 3)})

print(genetic_algorithm(result_list, finalGeneration))
