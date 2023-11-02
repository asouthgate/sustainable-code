# -*- coding: utf-8 -*-
# Copyright (C) Alex Southgate (2023)
#
# This file is part of an introductory tutorial on software design.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""This module contains some data processing code with several problems.

Code can easily get out of hand, so we should think about design principles ahead 
of time. What could we have done in advance in order to prevent this from happening?
"""

import sys


def filter_words(words, alphabet, threshold):
    """A docstring goes here that clearly dscribes the inputs & outputs.

    A further description could go here if required. You could include:

    Parameters
    ----------

    Returns
    -------

    Including something meaningful & consistent is more important than 
    choice of format.
    """
    raise NotImplementedError


def alignment_distance(s1, s2, indel_cost=1):
    """Given two strings, compute the alignment distance.

    For an indel cost of 1, the alignment distance is the
    edit distance. For indel costs other than 1, the distance
    is not a metric.
    
    Parameters
    ----------
    s1: `string` or string-like iterable
    s2: `string` or string-like iterable
    
    Returns
    -------
    distance: `float`
    """
    A = [[0 for c in s2] for c in s1]

    # initialize the first row and column
    for cl in range(len(s2)):
        A[0][cl] = cl * indel_cost
    for cm in range(len(s1)):
        A[cm][0] = cm * indel_cost

    for cm in range(1, len(s1)):
        for cl in range(1, len(s2)):
            A[cm][cl] = min([
                A[cm-1][cl] + indel_cost,
                A[cm][cl-1] + indel_cost,
                A[cm-1][cl-1] + (not s1[cm-1] == s2[cl-1])
            ])
    distance = A[-1][-1]
    return distance


if __name__ == "__main__":

    args = sys.argv
    tokens = sys.argv[1:]
    found = []
    alphabet = {c for c in "".join(tokens)}
        
    if args[1] == "2023-02-01_tokens":
        try:
            # READ THE WORDS
            with open("2023-02-01_tokens") as input_file:
                for li, line in enumerate(input_file):
                    words = line.rstrip().split(" ")

                    # FILTER OUT WORDS IF JACCARD TOO LOW
                    filtered = []
                    for word in words:
                        walpha = set(word)
                        J = len(walpha & alphabet) / len(walpha | alphabet)
                        if J > 0.3:
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

                            if A[-1][-1] < 2:
                                print(f"\033[92m Match \033[0mto token `{tokens[wi]}` found at line {li}: `{filtered[wi]}`")
                                found.add(tokens[wi])
        except:
            print("A mysterious bug 🪲 occurred :(")

        for token in tokens:
            if token not in found:
                print(f"\033[91m Failed \033[0mto find token `{token}`")

    else:
        try:
            # READ THE WORDS
            with open("2023-01-01_tokens") as input_file:
                for li, line in enumerate(input_file):
                    words = line.rstrip().split(" ")

                    # FILTER OUT WORDS IF JACCARD TOO LOW
                    filtered = []
                    for word in words:
                        walpha = set(word)
                        J = len(walpha & alphabet) / len(walpha | alphabet)
                        if J > 0.4:
                            filtered.append(word)
                            
                    # GET PAIRWISE DISTANCES
                    for wi in range(len(tokens)-1):
                        for wj in range(wi, len(filtered)):
                            # CALCULATE THE ALIGNMENT DISTANCE USING DYNAMIC PROGRAMMING
                            w1 = words[len(tokens)]
                            w2 = words[wj]
                            A = [[0 for c in w2] for c in w1]
                            for cl in range(len(w2)):
                                A[0][cl] == cl * 2
                            for cm in range(len(w1)):
                                A[cm][0] == cm * 2
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
            print("A mysterious bug 🪲 occurred :(")

        for token in tokens:
            if token not in found:
                print(f"\033[91m Failed\033[0m to find token `{token}`")

