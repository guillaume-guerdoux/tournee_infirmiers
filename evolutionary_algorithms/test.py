import pickle
from datetime import time

''' T : matrix : transfer duration between two heals
    K : integer : number of nurses
    P : integer : number of heals
    D : vector : heal duration (in seconds)
    N : integer : working duration per day of a nurse (in seconds)
    h : time : working time begin
    mandatory_schedule : dict : time constraints for heals
'''

with open('matrix_test', 'rb') as test:
    depickler_test=pickle.Unpickler(test)
    T=depickler_test.load()

K=5
P=30
D=[1800, 3600, 3600, 2700, 5400, 1800, 3600, 3600, 3600, 1800, 1800, 5400, 3600, 900, 1800, 2700, 1800, 3600, 2700, 3600, 1800, 3600, 3600, 2700, 5400, 1800, 3600, 3600, 3600, 1800]
N=28800
h=time(8,0,0)
mandatory_schedule={0: None, 1: (time(8,0,0), time(9,30,0)), 2: None, 3: (time(12,0,0), time(15,0,0)), 4: None, 5: (time(12,30,0), time(14,0,0)), 6: None, 7: (time(8,30,0), time(10,0,0)), 8: None, 9: None, 10: None, 11:None, 12: (time(8,30,0), time(10,0,0)), 13: None, 14: None, 15:None, 16: (time(13,30,0), time(15,0,0)), 14: None, 15:None, 16: (time(8,0,0), time(10,0,0)), 17:None, 18:None, 19:None, 20: None, 21:None, 22: (time(11,30,0), time(14,0,0)), 23: None, 24: None, 25:None, 26: (time(11,0,0), time(13,0,0)), 27: None, 28:None, 29:None}