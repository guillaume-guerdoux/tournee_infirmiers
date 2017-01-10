''' Functions : Generate random population
                Fitness Function
                Selection Function
                Mutation Function
                Cross Over Function
                Main Function '''
import numpy as np
import random
import copy

nurse_nb = 3
heal_nb = 15
distance_matrix = np.random.rand(heal_nb, heal_nb)
# mandatory_schedules = {0: None, 1: (8, 9), 2: (10, 11) ....}


def split_randomly_list(list_to_split, split_parts):
    new_list = []
    random.shuffle(list_to_split)
    for i in range(split_parts):
        if i == split_parts - 1:
            new_list.append(list_to_split)
            list_to_split = []
        else:
            if list_to_split:
                random_number = random.randint(0, len(list_to_split)-1)
                new_list.append(list_to_split[:random_number])
                del list_to_split[:random_number]
            else:
                new_list.append([])
    return new_list


def generate_random_population(population_nb):
    population = []
    heal_values = range(heal_nb)
    for sample in range(population_nb):
        temp_heal_values = list(heal_values)
        sample_list = split_randomly_list(temp_heal_values, nurse_nb)
        population.append(sample_list)
    return population


def fitness_function(sample):
    for nurse in sample:
        if nurse:
            return 1
        else:
            return 0


def mutation(sample):
    first_nurse = sample[random.randint(0, nurse_nb-1)]
    second_nurse = sample[random.randint(0, nurse_nb-1)]
    if not first_nurse and second_nurse:
        second_heal = second_nurse[random.randint(0, len(second_nurse)-1)]
        first_nurse.append(second_heal)
        second_nurse.remove(second_heal)
    if not second_nurse and first_nurse:
        first_heal = first_nurse[random.randint(0, len(first_nurse)-1)]
        first_nurse.remove(first_heal)
        second_nurse.append(first_heal)
    if first_nurse and second_nurse:
        first_heal = first_nurse[random.randint(0, len(first_nurse)-1)]
        second_heal = second_nurse[random.randint(0, len(second_nurse)-1)]
        first_nurse.remove(first_heal)
        first_nurse.append(second_heal)
        second_nurse.remove(second_heal)
        second_nurse.append(first_heal)


def tournament_selection(population, fitness_weight):
    random.shuffle(population)
    tournament_population = population[:int(len(population)/2)]
    new_population = copy.deepcopy(population[int(len(population)/2):])
    for i in range(0, len(tournament_population)-1, 2):  # last one is dead
        victory = random.random()
        first_fighter = tournament_population[i]
        second_fighter = tournament_population[i+1]
        if fitness_function(first_fighter) >= fitness_function(second_fighter):
            favourite_fighter = first_fighter
            loser_fighter = second_fighter
        else:
            favourite_fighter = second_fighter
            loser_fighter = first_fighter
        if victory >= (1-fitness_weight):
            new_population.append(favourite_fighter)
        else:
            new_population.append(loser_fighter)
    return new_population

initial_population = generate_random_population(4)
print("Initial population : ", initial_population)
print("New population : ", tournament_selection(initial_population, 0.7))
sample = [[1, 2], [3, 5], []]
print(sample)
mutation(sample)
print(sample)
