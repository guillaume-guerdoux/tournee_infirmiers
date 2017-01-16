import unittest
from evolutionary_algorithm import EvolutionaryOptimizer
import numpy as np
from datetime import timedelta
from datetime import time


class EvolutionaryOptimizerTests(unittest.TestCase):

    def setUp(self):
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
        self.evolutionary_optimizer = \
            EvolutionaryOptimizer(nurse_nb=3, heal_nb=10,
                                  time_distance_matrix=time_distance_matrix,
                                  heal_duration_vector=heal_duration_vector,
                                  mandatory_schedules=mandatory_schedules)

    def test_evolutionary_optimizer_generate_random_population(self):
        initial_population = \
            self.evolutionary_optimizer.generate_random_population(100)
        self.assertEqual(len(initial_population), 100)
        heal_set = {i for i in range(10)}
        for sample in initial_population:
            self.assertEqual(len(sample), 3)

    def test_evolutionary_optimizer_time_plus(self):
        time_test = time(hour=9, minute=30)
        first_timedelta = timedelta(minutes=20)
        second_timedelta = timedelta(minutes=5, seconds=30)
        new_time = self.evolutionary_optimizer.time_plus(time_test,
                                                         first_timedelta +
                                                         second_timedelta)
        self.assertEqual(new_time, time(hour=9, minute=55, second=30))

    def test_evolutionary_optimizer_event_overlaping_bad_order_01(self):
        is_overlapping = self.evolutionary_optimizer.event_overlaping(0, 1)
        self.assertEqual(is_overlapping, True)

    def test_evolutionary_optimizer_event_overlaping_no_problem_10(self):
        is_overlapping = self.evolutionary_optimizer.event_overlaping(1, 0)
        self.assertEqual(is_overlapping, False)

    def test_evolutionary_optimizer_event_overlaping_bad_order_21(self):
        is_overlapping = self.evolutionary_optimizer.event_overlaping(2, 1)
        self.assertEqual(is_overlapping, True)

    def test_evolutionary_optimizer_event_overlaping_no_problem_12(self):
        is_overlapping = self.evolutionary_optimizer.event_overlaping(1, 2)
        self.assertEqual(is_overlapping, False)

    def test_evolutionary_optimizer_event_overlaping_overlapping_14(self):
        is_overlapping = self.evolutionary_optimizer.event_overlaping(1, 4)
        self.assertEqual(is_overlapping, True)

    def test_evolutionary_optimizer_event_overlaping_overlapping_41(self):
        is_overlapping = self.evolutionary_optimizer.event_overlaping(4, 1)
        self.assertEqual(is_overlapping, True)

    def test_evolutionary_optimizer_event_overlaping_overlapping_09(self):
        is_overlapping = self.evolutionary_optimizer.event_overlaping(0, 9)
        self.assertEqual(is_overlapping, True)

    def test_evolutionary_optimizer_event_overlaping_overlapping_90(self):
        is_overlapping = self.evolutionary_optimizer.event_overlaping(9, 0)
        self.assertEqual(is_overlapping, True)

    def test_evolutionary_optimizer_schedules_respect_no_problem(self):
        nurse = [0, 1, 2]
        overlapping_heals = \
            self.evolutionary_optimizer.schedules_respect(nurse)
        self.assertEqual(overlapping_heals, 0)

    def test_evolutionary_optimizer_schedules_respect_no_respects(self):
        nurse = [0, 1, 9]
        overlapping_heals = \
            self.evolutionary_optimizer.schedules_respect(nurse)
        self.assertEqual(overlapping_heals, 1)
