from evolutionary_algorithm import EvolutionaryOptimizer
import numpy as np
from datetime import timedelta
from datetime import time

time_distance_matrix = np.loadtxt('time_distance_matrix')
heal_duration_vector = [timedelta(minutes=30) for i in range(10)]
# Nurse has to be there at this time
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

heal_overlapping = 0
no_heal_for_a_nurse = 0
for i in range(50):
    last_population = evolutionary_optimizer.population_evolution(5000)
    print(last_population[0])
    print("Fitness function :",
          evolutionary_optimizer.fitness_function(last_population[0]))
    for nurse in last_population[0]:
        if len(nurse) != 0:
            if (0 in nurse and 9 in nurse) or (1 in nurse and 4 in nurse) \
                    or (2 in nurse and 7 in nurse) or \
                    (4 in nurse and 6 in nurse):
                heal_overlapping += 1
        else:
            no_heal_for_a_nurse += 1
print("heal overlapping = ", heal_overlapping)
print("no_heal_for_a_nurse = ", no_heal_for_a_nurse)
