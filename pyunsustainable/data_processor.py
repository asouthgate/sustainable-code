# -*- coding: utf-8 -*-
# Copyright (C) Alex Southgate (2023)
#
# This file is part of an introductory tutorial on software design.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""This module contains some data processing code with a number of problems.

Code can easily get out of hand, so we should think about design principles ahead 
of time. What could we have done in advance in order to prevent this from happening?
"""

import sys

tokens = sys.argv[1:]
alphabet = {c for c in "".join(tokens)}
    
if args[1] == "new":
    try:
        # READ THE WORDS
        with open("2023-02-01_sequences.fa") as input_file:
            for li, line in enumerate(input_file):
                words = line.rstrip().split(" ")

                # FILTER OUT WORDS IF JACCARD TOO LOW
                filtered = []
                for word in words:
                    walpha = set(word)
                    J = len(walpha & alphabet) / len(walpha | alphabet)
                    if J >= 0.9:
                        filtered.append(word)
                        
                # GET PAIRWISE DISTANCES
                for wi in range(len(tokens)-1):
                    for wj in range(wi, len(filtered)):
                        # CALCULATE THE EDIT DISTANCE USING DYNAMIC PROGRAMMING
                        w1 = words[wi]
                        w2 = words[wj]
                        A = [[0 for c in w2] for c in w1]
                        for cl in range(len(w2)):
                            A[0][cl] == cl
                        for cm in range(len(w1)):
                            A[cm][0] == cm
                        for cm in range(1, len(w1)):
                            for cl in range(1, len(w2)):
                                A[cm][cl] = min([
                                    A[cm-1][cl] + 1,
                                    A[cm][cl-1] + 1,
                                    A[cm-1][cl-1] + (not w1[cm] == w1[cl])
                                ])
                        if A[-1][-1] < 3:
                            print(f"Match {tokens[wi]} found at line {li}: {filtered[wi]}")
    except:
        print("error")
elif args[1] == "old":
    try:
        # READ THE WORDS
        with open("2023-01-01_sequences.fa") as input_file:
            for li, line in enumerate(input_file):
                words = line.rstrip().split(" ")

                # FILTER OUT WORDS IF JACCARD TOO LOW
                filtered = []
                for word in words:
                    walpha = set(word)
                    J = len(walpha & alphabet) / len(walpha | alphabet)
                    if J >= 0.8:
                        filtered.append(word)
                        
                # GET PAIRWISE DISTANCES
                for wi in range(len(tokens)-1):
                    for wj in range(wi, len(filtered)):
                        # CALCULATE THE ALIGNMENT DISTANCE USING DYNAMIC PROGRAMMING
                        w1 = words[wi]
                        w2 = words[wj]
                        A = [[0 for c in w2] for c in w1]
                        for cl in range(len(w2)):
                            A[0][cl] == cl
                        for cm in range(len(w1)):
                            A[cm][0] == cm
                        for cm in range(1, len(w1)):
                            for cl in range(1, len(w2)):
                                A[cm][cl] = min([
                                    A[cm-1][cl] + 2,
                                    A[cm][cl-1] + 2,
                                    A[cm-1][cl-1] + (not w1[cm] == w1[cl])
                                ])
                        if A[-1][-1] < 3:
                            print(f"Match {tokens[wi]} found at line {li}: {filtered[wi]}")
    except:
        print("error")
