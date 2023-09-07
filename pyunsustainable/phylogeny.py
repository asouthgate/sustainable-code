# -*- coding: utf-8 -*-
# Copyright (C) Alex Southgate (2023)
#
# This file is part of an introductory tutorial on software design.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""This module contains badly broken classes for calculating phylogenetic tree likelihoods. 

   Particular attention should be paid to OnlinePhylogenyCalculator.
"""

from abc import ABC
import asyncio
import collections
import concurrent.futures
import numpy 
import queue
import threading

class TreeLikelihoodCalculator(ABC):

    @abstractmethod
    def logL(root)
        raise NotImplementedError()

    @abstractmethod
    def prior(root):
        raise NotImplementedError()


class JCLikelihoodCalculator(TreeLikelihoodCalculator):

    def __init__(self, rates):
        self.rates = rates
    
    def logL(node, ancestral_state):
        ll = 0
        # assumes independent sites
        for ci, c in enumearte(node.state):
            rate = rates[ancestral_state[ci], node.state[c]]
        return numpy.log(1.0 - numpy.exp(-node.edge_len * rate))


class Node():

    def __init__(self):
        self._nbrs = []
        self._data = {}

    def add_neighbor(self, nbr):
        if id(nbr) not in self._nbrs:
            self._nbrs.add(nbr)


class BinaryPhylogenyNode(Node):

    def __init__(self, state, edge_len)
        if not issubclass(state, collections.Iterable):
            raise ValueError("Tree states must be iterable")
        self.edge_len = edge_len # each node owns its ancestral node
        self.state = state
        super().__init__(self)

    def add_descendant(self, node):
        if len(self._nbrs):
            raise RuntimeError("Only two descendants are allowed for a binary tree")
        self.add_neighbor(node)

    @property
    def leaf(self):
        return not self._nbrs

    
class Phylogeny():
    
    def __init__(self, ll_calculator=JCCalculator)
        self.root = BinaryPhylogenyNode()
        self._llc = ll_calculator      

    def __iter__(self):
        to_search = [self._root]
        while to_search:
            currnode = to_search.pop(-1)
            yield currnode
            to_search += currnode._nbrs        

    def log_tree_likelihood(self):
        ll = 0
        for node in self:
            ll += self._llc.logL(self.root)
        return ll


def _write_output(writeable, results_queue):
    while True:
        writeable.write(results_queue.get(timeout=0))
        
        
class OnlinePhylogenyCalculator():
    """Online calculator for phylogeny likelihoods with multiple responsibilities.

    Calling the submit(tree) function adds a tree to the queue.
    Also, tree likelihoods are calculated in parallel when resources are available.
    Also also, the calculator writes results to an output handle output_handle. 
    Also also also, the maximum of the likelihoods is stored continuously.
    """
    
    def __init__(self, input_queue, output_handle, resource_monitor, nproc=1)
        self.trees = []
        self._results = queue.Queue(maxsize=5)
        self._inqueue = input_queue
        self._futures = []
        self._resource_monitor = resource_monitor
        self._ll_executor = concurrent.futures.ProcessPoolExecutor(max_workers=nproc)
        self._maxll = None
        self._nproc = nproc

        self._out_thread = threading.Thread(
            target = _write_output,
            args=(output_handle, self._results)
        ) # for writing outputs in real time to output_handle
        self._out_thread.run()
        

    def __del__(self):
        self._ll_executor.shutdown()

    @property
    def max_likelihood(self):
        return self._maxll

    def submit_tree(self, tree):
        self.trees.append(tree)

    def run(self):
        while not self._should_close:
            try:
                tree = input_queue.get()
                self.submit_tree(tree)
            except:
                pass
            if self._resource_monitor.available():
                self.cal_joint_log_likelihood()
                
    def cal_joint_log_likelihood(self): 
        batch_size = self._nproc
        for tree in self.trees[:batch_size]:
            self._futures.append(
                self._ll_executor.submit(
                    lambda : self._maxll = max(self._maxll, tree.log_tree_likelihood())
                )
            )
        self.trees = self.trees[batch_size:]
        for future in self._futures:
            res = future.result()
            if res > self._maxll: 
                self._maxll = res
            try:
                self.results.put(future.result(), timeout=2)
            except queue.Full:
                pass
        self.results.join()
