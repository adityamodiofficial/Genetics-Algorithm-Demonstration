# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:36:35 2020
@author: Aditya
"""

import numpy
import ga
equation_inputs=[4,-2,3.5,5,-11,-4.7]
num_wts=6
#CREATING INITIAL POPULATION
sol_per_pop=8
pop_size = (sol_per_pop,num_wts) #8*6
new_population = numpy.random.uniform(low=-4.0, high=4.0, size=pop_size) #8*6
#STARTING GA
num_generations=50
num_parents_mating=4
for generation in range(num_generations):
    print('Generation ::', generation+1)
    # 1. Measuring the fitness of each chromosome
    fitness=ga.cal_pop_fitness(equation_inputs,new_population)#1*8 since we have taken
    # 8 solution per population i.e 8 chromosomes(solution) so 8 fitness values
    # are generated
    
    # 2. Selecting the best parents in the population for mating
    parents=ga.select_mating_pool(new_population,fitness,num_parents_mating)#4*6
    # since we choose 4 parents and each parents i.e chromosome have 6 genes so 4*6
    
    #-----------MATING---TO----GENERATE----OFFSPRING-------------#
    
    # 3. Generating next generation using crossover
    offspring_size=(pop_size[0]-parents.shape[0],num_wts) #4*6 
    offspring_crossover = ga.crossover(parents,offspring_size) 
    
    
    # 4. Adding some variations to the offsrping using mutation
    offspring_mutation = ga.mutation(offspring_crossover) 
    
    # we successfully produced 4 offspring from the 4 selected parents and 
    #we are ready to create the new population of the next generation
    
    #----Creating the new population based on the parents and offspring-------#
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation
    
    print("The best value::",(numpy.max(numpy.dot(new_population,equation_inputs))))
    
