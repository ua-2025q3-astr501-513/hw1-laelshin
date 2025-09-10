#!/usr/bin/env python3
#
# Please look for "TODO" in the comments, which indicate where you
# need to write your code.
#
# Part 3: Implement a Numerically Stable Quadratic Equation Solver (1 point)
#
# * Objective:
#   Implement a numerically stable quadratic equation solver that does
#   not catastrophic cancellation.
# * Details:
#   The description of the problem and the solution template can be
#   found in `hw1/p3.py`.
#
# From lecture `01w`, we learned about catastrophic cancellation---the
# significant loss of precision that occurs when subtracting two
# nearly equal numbers.
# This problem actually appeared in CK's research!
# While solving for the initial conditions of (unstable) spherical
# photon orbits around a black hole for the convergence test of
# [GRay2](https://ui.adsabs.harvard.edu/abs/2018ApJ...867...59C),
# catastrophic cancellation introduced errors so severe that photons
# would not remain on their spherical orbits for an radian.
# CK suspected a bug in the integrator and spent an entire month
# debugging the wrong part of the code.
# At the end, he realized the real problem.
# The standard quadratic formula we all learn in high school was
# simply not accurate enough for reliable numerical computation.
#
# Here, let's implement a numerically stable quadratic equation solver
# to overcome catastrophic cancellation.
# Please make sure that you take care of all the special cases.
import numpy as np

def quadratic(a, b, c):
    """Numerically stable quadratic equation solver

    The standard quadratic formula

        x = (-b +- sqrt(b^2 - 4ac)) / (2a)

    is algebraically correct but can suffer from *catastrophic
    cancellation* when b^2 >> 4ac and the sign of b matches the
    chosen +-.
    In that case, subtracting two nearly equal numbers causes a large
    loss of precision.

    A more stable alternative is obtained by multiplying top and
    bottom by the conjugate, leading to two equivalent forms.
    To avoid cancellation, choose the version that keeps the
    subtraction well-separated:

        x1 = (-b - sign(b) * sqrt(b^2 - 4ac)) / (2a)
        x2 = (c / a) / x1

    This way, at least one root is always computed stably.

    Args:
        a, b, c: coefficients for the quadratic equation
                 a x^2 + b x + c = 0.

    Returns:
        x1, x2: the two roots of the quadratic equation.
                If there are two real roots, x1 < x2.
                If there is only one real root, x2 == None.
                If there is no real root, x1 == x2 == None.
    """
    # TODO: implement the stable quadratic equation solver here
    # We should avoid the direct subtraction like b-b
    # x = (-b +-sqrt(b**2 - 4*a*c))/(2a) -> multiply 1 = (-b -+sqrt(b**2 - 4*a*c)) / (-b -+sqrt(b**2 - 4*a*c))
    # then, x = (2c) / (-b -+sqrt(b**2 - 4*a*c))
    # we can avoid the b - b calculation by selecting appropriate sign
    
    disc = b*b - 4*a*c

    # no real root case
    if disc < 0:
        x1 = None
        x2 = None
        return x1, x2
    # one real root case
     if disc == 0:
        x1 = -b / (2*a)
        return x1, None
         
    if b >= 0:
        x1 = (-1*b - np.sqrt(disc))/(2*a)
        x2 = (2*c)/(-1*b - np.sqrt(disc))

    elif b < 0:
        x1 = (2*c)/(-1*b + np.sqrt(disc))
        x2 = (-1*b + np.sqrt(disc))/(2*a)

    if np.isclose(x1, x2): # check whether x1 == x2
        x2 = None

    if x2 is not None and x1 > x2:
        x1, x2 = x2, x1
        
    return x1, x2
