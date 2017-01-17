from django.test import TestCase
import numpy as np
from datetime import timedelta
from datetime import time
# models
from optimizer.models import EvolutionaryOptimizer

class EvolutionaryOptimizerTests(TestCase):

    def test_evolutionary_optimizer_creation(self):
        identity =  np.identity(14)
        ones = np.ones(14)
        time_distance_matrix = ones -identity
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

    def test_evolutionary_optimizer_get_optimize_population(self):
        identity =  np.identity(14)
        ones = np.ones(14)
        time_distance_matrix = ones -identity
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
        print(evolutionary_optimizer.get_optimize_population())
