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
            return 0
        p = 0
        while (num >> p) & 1 == 0:
            p += 1
        return p

    def insert(self, ins_val):
        ''' Counts predicate bits in the inserted integer and replaces
            the value of the current bit stream if necessary.
        '''
        z = self.zeroes(ins_val)
        if (self.m[self.ticker] < z):
            self.m[self.ticker] = z
        if (self.ticker == (len(self.m) - 1)):
            self.ticker = 0
        else:
            self.ticker += 1

    def simple_harmonic_mean(self, input_arr):
        ''' Calculates the harmonic mean of the input array
        '''
        tot = 0.0
        for val in input_arr:
            tot += 1.0 / val

        return (len(input_arr) / tot)

    def cardinality_estimate(self):
        ''' Computes the estimated cardinality of the multiset'''
        stream_estimates = []

        for val in self.m:
            stream_estimates.append(2 ** val)

        return self.simple_harmonic_mean(stream_estimates)










