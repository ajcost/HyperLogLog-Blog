'''
A simple implementation of the HyperLogLog Algorithm
'''
import numpy as np

class HyperLogLog(object):
    ''' Attributes:
           m: array that holds the maximum number of preceding zeros per stream
           ticker: index that each new value is written to
    '''

    def __init__(self, m_n):
        ''' Initialize a HyperLogLog object where m_n is the number of streams.
        '''
        self.m = np.zeros(m_n, dtype=int)
        self.ticker = 0

    def zeroes(self, num):
        '''Counts the number of predicate 0 bits in integer.'''
        if num == 0:
            return 32 # Assumes 32 bit integer inputs!
        p = 0
        while (num >> p) & 1 == 0:
            p += 1
            return p

    def insert(self, ins_val):
        ''' Counts predicate bits in the inserted integer and replaces
            the value of the current bit stream if necessary.
        '''
        z = zeroes(ins_val)
        if (m[ticker] < z):
            m[ticker] = z
        if (ticker == 13):
            ticker = 0
        else:
            ticker += ticker

    def harmonic_mean(self):
        




