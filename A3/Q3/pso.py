


for particle in particle_list:
    initialize_particle(particle)

do
    for particle in particle_list:
        fitness = calculate_fitness(particle, particle_list)
        if fitness > personalBest:
            personalBest = fitness
    globalBest = max(particle_list)
    for particle in particle_list:
        currVelocity = particle.currVelocity +
        updatedVelocity =
