''' Functions : Generate random population
                Fitness Function
                Selection Function
                Mutation Function
                Cross Over Function
                Main Function '''
import numpy as np
import random
import copy
from datetime import time
import itertools

nurse_nb = 3
heal_nb = 10
no_symetric_distance_matrix = np.random.rand(heal_nb, heal_nb)
for i in range(heal_nb):
    no_symetric_distance_matrix[i][i] = 0
# mandatory_schedules = {0: None, 1: (8, 9), 2: (10, 11) ....}
distance_matrix = (no_symetric_distance_matrix +
                   no_symetric_distance_matrix.T)/2

mandatory_schedules = {0: None, 1: (time(8, 0, 0), time(9, 0, 0)),
                       2: (time(10, 0, 0), time(11, 0, 0)),
                       3: None, 4: (time(8, 30, 0), time(9, 30, 0)),
                       5: None, 6: None, 7: (time(10, 30, 0), time(12, 0, 0)),
                       8: None, 9: (time(19, 0, 0), time(20, 0, 0))}


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


def event_overlaping(first_event, second_event):
    if first_event is None or second_event is None:
        return False
    else:
        first_event_start_time = first_event[0]
        first_event_end_time = first_event[1]
        second_event_start_time = second_event[0]
        second_event_end_time = second_event[1]
        if first_event_end_time < second_event_start_time:
            return False
        elif first_event_start_time > second_event_end_time:
            return False
        else:
            return True


def fitness_function(sample):
    no_heal_for_a_nurse = 0
    overlapping_heals_for_a_nurse = 0
    for nurse in sample:
        if nurse:
            for paire in itertools.combinations(nurse, 2):
                if event_overlaping(mandatory_schedules[paire[0]],
                                    mandatory_schedules[paire[1]]):
                    overlapping_heals_for_a_nurse += 1
        else:
            no_heal_for_a_nurse += 1
    return 10*no_heal_for_a_nurse + 5*overlapping_heals_for_a_nurse


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


# TODO : To much empty list : solve this
def cross_over_function(first_parent, second_parent):
    child = []
    added_genes = []
    random.shuffle(first_parent)
    random.shuffle(second_parent)
    for gene in range(len(first_parent)):
        first_parent_gene = first_parent[gene]
        second_parent_gene = second_parent[gene]
        combination = list(set(first_parent_gene).union(second_parent_gene))
        non_redondant_gene = []
        for allele in combination:
            if allele not in added_genes:
                non_redondant_gene.append(allele)
        child.append(non_redondant_gene)
        added_genes.extend(non_redondant_gene)
    return child


# TODO : Take into account diffence between fitness function
def tournament_selection(population, fitness_weight):
    random.shuffle(population)
    new_population = []
    # tournament_population = population[:int(len(population)/2)]
    # new_population = copy.deepcopy(population[int(len(population)/2):])
    for i in range(0, len(population)-1, 2):  # last one is dead
        print(i)
        victory = random.random()
        first_fighter = population[i]
        second_fighter = population[i+1]
        if fitness_function(first_fighter) <= fitness_function(second_fighter):
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


def population_evolution(population_nb):
    population = generate_random_population(population_nb)
    print("Initial population : ", population)
    while(len(population) != 1):
        print(len(population))
        # Tournament
        population = tournament_selection(population, 0.9)
        print("Tournament population: ", population)
        # Mutation : 0.5 probability
        for sample in population:
            mutation_probability = random.random()
            if mutation_probability > 0.5:
                mutation(sample)
        random.shuffle(population)
        for i in range(0, len(population)-1, 2):
            first_parent = population[i]
            second_parent = population[i+1]
            population.append(cross_over_function(first_parent, second_parent))

    print("Finish", population)

if __name__ == "__main__":
    # print(distance_matrix)
    population_evolution(1000)
    '''print(initial_population[3])
    print("Initial population : ", initial_population)
    new_population = tournament_selection(initial_population, 0.7)
    print("Tournament population: ", new_population)'''
