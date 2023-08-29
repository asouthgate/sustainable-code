# -*- coding: utf-8 -*-
# Copyright (C) Alex Southgate (2023)
#
# This file is part of an introductory tutorial on software design.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""This module contains broken tests for a broken implementation of the
Jacobi method for iterative solution of a system of linear equations.

With some additions, these tests could be useful
"""

import numpy
from pybroken import jacobi


def test_jacobi_exceptions():
    pass


def test_jacobi_args():
    pass


def test_jacobi_system():
    """Test that the solver works correctly for a simple system."""

    m = 5
    A = numpy.zeros((m, m))
    b = numpy.ones(m)
    js = jacobi.JacobiSolver(A)
    x = js.solve(b, 0.1, 100)

    assert len(x) == 5
    
    
