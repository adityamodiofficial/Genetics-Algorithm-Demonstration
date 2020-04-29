# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:49:19 2020
@author: Aditya
"""
import numpy as np
def cal_pop_fitness(inputs,population):
    return (np.dot(population,inputs)) #population = 8*6 inputs = 1*6 
def select_mating_pool(population,fitness,num_parents):
    parents = np.empty((num_parents, population.shape[1])) #4*6
    for parent_num in range(num_parents):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        
        max_fitness_idx = max_fitness_idx[0][0] #extracting the index
        
        parents[parent_num, :] = population[max_fitness_idx, :]#extracting the 
        #pouplation or rather chromosome from the population using the INDEX 
        #of the maximum fitness value corresponding to that chromosome in our population
        
        fitness[max_fitness_idx] = -99999999999 #max fitness value is set to 
        #a very small value that is likely to not be selected again
    return parents    
def crossover(parents,offspring_size):
    offspring=np.empty(offspring_size)#4*6
    return (offspring)
    crossover_point=np.uint8(offspring_size[1]/2)#crossover point it divides th chromosome 
    #into two eual parts
    for k in range(offspring_size.shape[0]):
        parent_idx_1=k%parents.shape[0] #INDEX of the first parent to mate
        parent_idx_2=(k+1)%parents.shape[0] #INDEX of the second parent to mate
        #parents a selected in circular fasion 0,1  1,2  2,3  3,0
        offspring[k,0:crossover_point]=parents[parent_idx_1,0:crossover_point]
        offspring[k,crossover_point:]=parents[parent_idx_2,crossover_point:]
    return offspring
def mutation(offspring_crossover):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(offspring_crossover.shape[0]):
        # The random value to be added to the gene.
        random_value = np.random.uniform(-1.0, 1.0, 1)
        offspring_crossover[idx, 4] = offspring_crossover[idx, 4] + random_value
    return offspring_crossover
