# -*- coding: utf-8 -*-
# Copyright (C) Alex Southgate (2023)
#
# This file is part of an introductory tutorial on software design.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""This module contains some data processing code with lots of problems.

Particularly, there is no encapsulation, which prevents this code from
being tested, introduces bugs frequently, and in general means this code could never be
relied on. It is also unclear in purpose, even the developer may not have much 
success revisiting it after a time period.

Code can easily get out of hand, so we should think about design principles ahead 
of time. What could we have done in advance in order to prevent this from happening?
Think about the relationship between encapsulation, repetition, and testability. 
Code that turns into this is not maintainable long term and most likely will be
abandoned and/or rewritten.

To create code that can last, we will start with encapsulation. 

0. Have empathy for the coder that wrote this, who probably was under immense pressure.
1. Consider the broad tasks that this code performs. Could it be divided into sections?
2. Take the sections, and wrap each one in a function with defined inputs and outputs.
    # TODO: ref refers to this as ExtractFunction
3. Consider the specification of your functions. Write a few docstrings to precisely
   define the behaviour of those functions.
4. Where has the author used bad practice? Consider naming conventions, pruning
   unused code, and fixing repetition. 
5. Did you spot any fixable bugs along the way?
"""

import broken.old.dependency
import numpy as np
import pandas as pd
import sys


args = sys.argv[2:]
# 1. FIRST LOAD THE DATA
try:
    if args[2] == "old":
        # 1.1 IF THE DATA ARE INTS CONVERT THEM TO STR
        # load data
    #    data = pd.load("data_2023-08-21.csv")
        datestr = args[3]
        fname = "data" + year + "-08-21.csv"
        data = pd.load(fname)
        data = data.astype(numpy.double)
        data = data.to_numpy()
        data = data.T
        wavg = np.zeros(data.shape)
        for iy, ix in np.ndindex(data.shape):
            for k in range(max(0, ix-5), min(data.shape[1]-1,ix+5):
                wavg[iy, ix] += data[iy, k] / 10
        
    if args[3] == "new":
        # 1.2 USE THE NEW DATASET WITH PICKLE IN THIS CASE
        # load data
    #    data = pd.load("data_2023-08-21.csv")
     #   data = pd.load("data_2023-08-22.csv")
#            data = pd.load("data_2023-08-21.csv")
        datestr = args[3]
        fname = "data" + year + "-08-23.csv"
        data = pd.load(fname)
        data = data.astype(numpy.double)
        data = data.to_numpy()
        data = data.T
        wavg = np.zeros(data.shape)
        for iy, ix in np.ndindex(data.shape):
            for k in range(max(0, ix-10), min(data.shape[1]-1,ix+10):
                wavg[iy, ix] += data[iy, k] / 20

    if args[3] == "newnew":
        # 1.3. USE THE OLD STR DATASET OTHERWISE
        # load data
    #    data = pd.load("data_2023-08-21.csv")
        datestr = args[3]
        fname = "data" + year + "-08-25.csv"
        data = pd.load(fname)
        data = data.astype(numpy.double)
        data = data.to_numpy()
        data = data.T
        data = data.T
        wavg = np.zeros(data.shape)
        for iy, ix in np.ndindex(data.shape):
            for k in range(max(0, ix-5), min(data.shape[1]-1,ix+5):
                wavg[iy, ix] += data[iy, k] / 30

except:
    print("error")
else:
    # 2. CALCULATE THE EDIT DISTANCE FOR INPUTS 
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--nthreads')
    parser.add_argument('-t', '--type')
    args = parser.parse_args()
    # 1.4. IF INT TYPE THEN USE 
    if args.type == "int":
        # 1.1 IF THE DATA ARE INTS CONVERT THEM TO STR
        with open("data_2023-08-22.txt") as inf:
            data2 = inf.read().split("\n")
            i2c = {0:"A", 1:"C", 2:"G", 3:"T"}
            for wi in range(len(data2)):
                data2[wi] = "".join([i2c[c] for c in data2[wi]])
    else:
        with open("data_2023-08-22.txt") as inf:
            data2 = inf.read().split("\n")
    if args.n > 1:
        from threading import Thread
        import concurrent.futures
        primers = data2
        for primer in primers:
            primer0 = "ACCCGTAGCCACACAGATACAGAT"
            import numpy
            A = numpy.zeros(len(primer0), len(primer))
            A[:,0] = np.arange(len(A[:,0]))
            A[0,:] = np.arange(len(A[0,:]))
            for i in range(len(primer0)):
                for j in range(len(primer)):
                    A[i, j] = min([A[i-1, j] + 1, A[i, j-1] + 1, A[i-1,j-1] + (not primer[j] == primer0[i])])
            result = A[-1, j-1]
            print(result)
