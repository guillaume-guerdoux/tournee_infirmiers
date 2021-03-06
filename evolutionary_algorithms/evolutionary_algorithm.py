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
from datetime import timedelta
from datetime import datetime
import itertools


'''
no_symetric_distance_matrix = np.random.rand(heal_nb, heal_nb)
for i in range(heal_nb):
    no_symetric_distance_matrix[i][i] = 0
# mandatory_schedules = {0: None, 1: (8, 9), 2: (10, 11) ....}
distance_matrix = (no_symetric_distance_matrix +
                   no_symetric_distance_matrix.T)/2'''


class EvolutionaryOptimizer:

    def __init__(self, nurse_nb, heal_nb,
                 time_distance_matrix, heal_duration_vector,
                 mandatory_schedules):
        self.nurse_nb = nurse_nb
        self.heal_nb = heal_nb
        self.time_distance_matrix = time_distance_matrix
        self.heal_duration_vector = heal_duration_vector
        self.mandatory_schedules = mandatory_schedules
        self.total_distance = 0
        self.possible_combinations = 0
        heal_values = range(self.heal_nb)
        for paire_heal in itertools.combinations(heal_values, 2):
            self.total_distance += \
                self.time_distance_matrix[paire_heal[0]][paire_heal[1]]
            self.possible_combinations += 1

    def split_randomly_list(self, list_to_split, split_parts):
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

    # Generate a random population
    def generate_random_population(self, population_nb):
        population = []
        heal_values = range(self.heal_nb)
        for sample in range(population_nb):
            temp_heal_values = list(heal_values)
            sample_list = self.split_randomly_list(temp_heal_values,
                                                   self.nurse_nb)
            population.append(sample_list)
        return population

    # Add a timedelta to a time
    def time_plus(self, time, timedelta):
        start = datetime(
            2000, 1, 1,
            hour=time.hour, minute=time.minute, second=time.second)
        end = start + timedelta
        return end.time()

    # For two events, return if they are overlapping
    # Worst case : nurse begin heal at the end of available window
    def event_overlaping(self, first_event, second_event):
        first_event_end_time = self.mandatory_schedules[first_event][1]
        first_event_duration = self.heal_duration_vector[first_event]
        second_event_end_time = self.mandatory_schedules[second_event][1]
        time_distance_between_heals = \
            timedelta(seconds=self.time_distance_matrix[first_event][second_event])
        first_event_taken_time = self.time_plus(first_event_end_time,
                                                first_event_duration +
                                                time_distance_between_heals)
        if first_event_taken_time > second_event_end_time:
            return True
        else:
            return False

    # Return how many heals are overlapping for one nurse
    def schedules_respect(self, nurse):
        overlapping_heals = 0
        heals_with_time_constraint = []
        for heal in nurse:
            if self.mandatory_schedules[heal] is not None:
                heals_with_time_constraint.append(heal)
        for paire in itertools.combinations(heals_with_time_constraint, 2):
            if self.event_overlaping(paire[0], paire[1]) and \
               self.event_overlaping(paire[1], paire[0]):
                overlapping_heals += 1
        return overlapping_heals

    # Fitness function : Algorithm goal is to minimize it
    def fitness_function(self, sample):
        no_heal_for_a_nurse = 0
        total_distance_covered = 0
        schedules_respect_nb = 0
        for nurse in sample:
            # Check if each nurse has heals to do
            if nurse:
                # Check overlapping
                schedules_respect_nb += self.schedules_respect(nurse)
                # Check total distance covered by a nurse
                for paire in itertools.combinations(nurse, 2):
                    total_distance_covered += \
                        self.time_distance_matrix[paire[0]][paire[1]]
            else:
                no_heal_for_a_nurse += 1
        cost = 5*(no_heal_for_a_nurse/self.nurse_nb) + \
            100*schedules_respect_nb/self.possible_combinations + \
            1*total_distance_covered/self.total_distance
        return(float(cost.__round__(2)))

    # Mutation for a sample
    def mutation(self, sample):
        first_nurse = sample[random.randint(0, self.nurse_nb-1)]
        second_nurse = sample[random.randint(0, self.nurse_nb-1)]
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

    # Cross over function : one child created for two samples
    # TODO : To much empty list : solve this
    def cross_over_function(self, first_parent, second_parent):
        child = []
        added_genes = []
        copy_first_parent = copy.deepcopy(first_parent)
        copy_second_parent = copy.deepcopy(second_parent)
        random.shuffle(copy_first_parent)
        random.shuffle(copy_second_parent)
        for gene in range(len(copy_first_parent)):
            first_parent_gene = copy_first_parent[gene]
            second_parent_gene = copy_second_parent[gene]
            combination = \
                list(set(first_parent_gene).union(second_parent_gene))
            non_redondant_gene = []
            for allele in combination:
                if allele not in added_genes:
                    non_redondant_gene.append(allele)
            child.append(non_redondant_gene)
            added_genes.extend(non_redondant_gene)
        return child

    # Kill half of the population by tournament
    def tournament_selection(self, population):
        random.shuffle(population)
        new_population = []
        # tournament_population = population[:int(len(population)/2)]
        # new_population = copy.deepcopy(population[int(len(population)/2):])
        for i in range(0, len(population)-1, 2):  # last one is dead
            victory = random.random()
            first_fighter = population[i]
            second_fighter = population[i+1]
            if self.fitness_function(first_fighter) <= \
                    self.fitness_function(second_fighter):
                favourite = first_fighter
                loser = second_fighter
            else:
                favourite = second_fighter
                loser = first_fighter
            if victory >= 0.9:
                new_population.append(loser)
            else:
                new_population.append(favourite)
        return new_population

    # Main function to call
    def population_evolution(self, population_nb):
        population = self.generate_random_population(population_nb)
        # print("Initial population : ", population)
        while(len(population) >= 3):
            # Tournament
            population = self.tournament_selection(population)
            # print("Tournament population: ", population)
            # Mutation : 0.5 probability
            for sample in population:
                mutation_probability = random.random()
                if mutation_probability > 0.8:
                    self.mutation(sample)
            random.shuffle(population)
            for i in range(0, len(population)-1, 2):
                first_parent = population[i]
                second_parent = population[i+1]
                population.append(self.cross_over_function(first_parent,
                                                           second_parent))

        return population


if __name__ == "__main__":
    # Matrix with time taken (in car) between each point : Referent : ALICE
    time_distance_matrix = np.loadtxt('time_distance_matrix')

    # Vector with each heal duration
    heal_duration_vector = [timedelta(minutes=30) for i in range(10)]

    # Time window when nurse has to arrive at client's home
    mandatory_schedules = {0: (time(19, 30, 0), time(20, 30, 0)),
                           1: (time(8, 0, 0), time(9, 0, 0)),
                           2: (time(10, 0, 0), time(11, 0, 0)),
                           3: None, 4: (time(8, 30, 0), time(9, 30, 0)),
                           5: None, 6: (time(9, 45, 0), time(10, 0, 0)),
                           7: (time(10, 30, 0), time(11, 30, 0)),
                           8: None, 9: (time(19, 0, 0), time(20, 30, 0))}
    evolutionary_optimizer = \
        EvolutionaryOptimizer(nurse_nb=3, heal_nb=10,
                              time_distance_matrix=time_distance_matrix,
                              heal_duration_vector=heal_duration_vector,
                              mandatory_schedules=mandatory_schedules)

    # Algorithm runs until it find a good candidate
    i = 0
    stop = False
    while not stop and i < 10:
        print("Iteration #{}".format(i + 1))
        population = evolutionary_optimizer.population_evolution(10000)[0]
        # print(population)
        stop = True
        for nurse in population:
            if evolutionary_optimizer.schedules_respect(nurse) != 0:
                stop = False
        i += 1
    print("Finish", population)
