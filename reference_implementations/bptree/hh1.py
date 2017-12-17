"""
Implementation of BPTree based on the paper by Braverman et al
"""
import random
from math import floor,log

class HH1(object):

    def __init__(self, sigma, stream, n):
        # Setting up constants and variables we need later
        self.sigma = sigma
        self.stream = stream
        self.n = n
        self.R = self.calculate_R()
        self.Z = self.generate_Z()
        self.b = [0]*(self.R+1)
        self.X = (0,0)
        self.r = 1
        self.H = -1
        self.Beta = (3/4)
        self.c = (1/32)

    def compute_next(self, item):
        # If we figured out all the bits quit
        if self.r >= self.R:
            return b

        match = True

        for j in range(self.r):
            # Check if this matches what we know of the HH thus far
            if self.hash_func(item, j) != self.b[j]:
                match = False
                break

            # If it does match the HH record the next bit of this item
            if match:
                self.H = self.item
                self.X[self.hash_func(item, self.r)] = \
                        self.X[hash_func(item, self.r)] + self.Z[item]

            # If we've seen enough items for the HH to have made itself known then
            # record the next bit into b
            if abs(self.X[0] + self.X[1]) >= (self.c * self.sigma * self.Beta**self.r):
                # Record the bit
                self.b[r] = 1 if (abs(self.X[1]) > abs(self.X[0])) else 0
                # Refresh everything
                self.X = (0,0)
                self.r = self.r + 1
                self.Z = self.generate_Z(n)

    def get_value(self):
        return self.H

    def hash_func(self, item, bit):
        raise NotImplementedError

    def calculate_R(self):
        return 3*floor(log(min(self.n,self.sigma**2)+1,2))

    def generate_Z(self):
        z = []
        for i in range(self.n+1):
            # TODO: Talk to Bailey about this method of randomness
            z.append(random.choice([1,-1]))
        return z

