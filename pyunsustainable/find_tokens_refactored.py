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


def jaccard_index(A: set, B: set) -> float:
    """Calculate the Jaccard index between sets A and B."""
    return len(A & B) / len(A | B)


def filter_words(words, alphabet, threshold):
    """Filter out words with characters too different to a reference set.

    Parameters:
    ----------
    words: `list` of words to filter
    reference: `set` of characters
    threshold: `float` cutoff

    Returns:
    -------
    filtered: `list` of filtered words
    """
    filtered = []
    for word in words:
        walpha = set(word)
        if jaccard_index(walpha, alphabet) >= threshold:
            filtered.append(word)
    return filtered


def alignment_distance(s1, s2, indel_cost=1):
    """Given two strings, compute the alignment distance.

    For an indel cost of 1, the alignment distance is the
    edit distance. For indel costs other than 1, the distance
    is not a metric.
    
    Parameters:
    ----------
    s1: `string` or string-like iterable
    s2: `string` or string-like iterable
    
    Returns:
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


def search_file_words(file_path, words, filter_t=0.3, edit_dist=1, indel_cost=1):
    """Search for words in a file.

    If edit_dist > 0, approximate matches are allowed.

    Parameters
    ----------
    file_path: `str`
    words: `list` of words to search for
    filter_t: `float` threshold in the interval [0,1]. Use 0 for no filtering.
    indel_cost: a positive `float`. Use 1 for the edit distance.

    Returns
    -------
    matches: `list` of `tuple` (line number, matching word)

    """
    found = []
    try:
        with open(file_path) as input_file:
            for li, line in enumerate(input_file):
                words = line.rstrip().split(" ")
                filtered = filter_words(words, alphabet, filter_t)
                for wi in range(len(tokens)):
                    for wj in range(len(filtered)):
                        dist = alignment_distance(tokens[wi], filtered[wj], indel_cost)
                        if dist <= edit_dist:
                            # What's wrong with this?
                            found.append((li, line, tokens[wi], filtered[wj])) 
    except FileNotFoundError:
        print(f"No such file: {file_path}")
    return found


def print_results(results):
    # What if we want to print the specific tokens that were not found?
    if not results:
        print(f"\033[91m Failed \033[0mto find a result")
    # Could this be done in a better way?
    for lineno, line, token, matching_word in results:
        print(f"\033[92m Match \033[0mto token `{token}` found at line {lineno}: `{matching_word}`")


if __name__ == "__main__":

    args = sys.argv
    tokens = sys.argv[1:]
    alphabet = {c for c in "".join(tokens)}

    # What is the problem with hard-coding filenames?
    results = search_file_words("2023-02-01_tokens", tokens)
    print_results(results)

