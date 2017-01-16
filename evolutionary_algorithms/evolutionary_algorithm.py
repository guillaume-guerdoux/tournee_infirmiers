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


class EvolutionaryOptimizer:

    def __init__(self, nurse_nb, heal_nb,
                 time_distance_matrix, heal_duration_vector,
                 mandatory_schedules):
        self.nurse_nb = nurse_nb
        self.heal_nb = heal_nb
        self.time_distance_matrix = time_distance_matrix
        self.heal_duration_vector = heal_duration_vector
        self.mandatory_schedules = mandatory_schedules

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

    def generate_random_population(self, population_nb):
        population = []
        heal_values = range(self.heal_nb)
        for sample in range(population_nb):
            temp_heal_values = list(heal_values)
            sample_list = self.split_randomly_list(temp_heal_values,
                                                   self.nurse_nb)
            population.append(sample_list)
        return population

    def time_plus(self, time, timedelta):
        start = datetime(
            2000, 1, 1,
            hour=time.hour, minute=time.minute, second=time.second)
        end = start + timedelta
        return end.time()

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

    def fitness_function(self, sample):
        no_heal_for_a_nurse = 0
        total_distance_covered = 0
        schedules_respect_nb = 0
        for nurse in sample:
            # Check if each nurse has heals to do
            if nurse:
                # Check overlapping
                if self.schedules_respect(nurse):
                    schedules_respect_nb += 1
                # Check total distance covered by a nurse
                for heal_index in range(len(nurse) - 2):
                    total_distance_covered += \
                        self.time_distance_matrix[heal_index][heal_index+1]
            else:
                no_heal_for_a_nurse += 1
        return(10*no_heal_for_a_nurse +
               20*schedules_respect_nb +
               2*total_distance_covered)

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
            combination = list(set(first_parent_gene).union(second_parent_gene))
            non_redondant_gene = []
            for allele in combination:
                if allele not in added_genes:
                    non_redondant_gene.append(allele)
            child.append(non_redondant_gene)
            added_genes.extend(non_redondant_gene)
        return child

    def tournament_selection(self, population):
        random.shuffle(population)
        new_population = []
        # tournament_population = population[:int(len(population)/2)]
        # new_population = copy.deepcopy(population[int(len(population)/2):])
        for i in range(0, len(population)-1, 2):  # last one is dead
            victory = random.random()
            first_fighter = population[i]
            second_fighter = population[i+1]
            try:
                first_fighter_victory_probability = \
                    self.fitness_function(second_fighter) / \
                    (self.fitness_function(first_fighter) +
                     self.fitness_function(second_fighter))
            except ZeroDivisionError:
                first_fighter_victory_probability = 0.5
            if victory <= (first_fighter_victory_probability):
                new_population.append(first_fighter)
            else:
                new_population.append(second_fighter)
        return new_population

    # Chance to win is proportionnal to fitness function differences
    def population_evolution(self, population_nb):
        population = self.generate_random_population(population_nb)
        print("Initial population : ", population)
        while(len(population) >= 10):
            # Tournament
            population = self.tournament_selection(population)
            # print("Tournament population: ", population)
            # Mutation : 0.5 probability
            for sample in population:
                mutation_probability = random.random()
                if mutation_probability > 0.5:
                    self.mutation(sample)
            random.shuffle(population)
            for i in range(0, len(population)-1, 2):
                first_parent = population[i]
                second_parent = population[i+1]
                population.append(self.cross_over_function(first_parent,
                                                           second_parent))

        print("Finish", population)

if __name__ == "__main__":
    time_distance_matrix = np.loadtxt('time_distance_matrix')
    heal_duration_vector = [timedelta(minutes=30) for i in range(10)]
    # Nurse has to be there at this time
    mandatory_schedules = {0: (time(19, 30, 0), time(20, 30, 0)),
                           1: (time(8, 0, 0), time(9, 0, 0)),
                           2: (time(10, 0, 0), time(11, 0, 0)),
                           3: None, 4: (time(8, 30, 0), time(9, 30, 0)),
                           5: None, 6: None,
                           7: (time(10, 30, 0), time(12, 0, 0)),
                           8: None, 9: (time(19, 0, 0), time(20, 0, 0))}
    evolutionary_optimizer = \
        EvolutionaryOptimizer(nurse_nb=3, heal_nb=10,
                              time_distance_matrix=time_distance_matrix,
                              heal_duration_vector=heal_duration_vector,
                              mandatory_schedules=mandatory_schedules)
    # print(time_distance_matrix)
    evolutionary_optimizer.population_evolution(5000)
    '''print(initial_population[3])
    print("Initial population : ", initial_population)
    new_population = tournament_selection(initial_population, 0.7)
    print("Tournament population: ", new_population)'''
