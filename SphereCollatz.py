# -------
# imports
# -------

import sys

# from Collatz import collatz_solve

# ----
# main
# ----


#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read two ints
    r is a reader
    return a list of the two ints, otherwise a list of zeros
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_eval
# ------------

array = [0] * 1000000

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i, j > 0
    assert i, j < 1000000

    cycle = 1
    max_cycle = 1
    x = 0

    #swap values
    if (i > j) :
        a = j
        j = i
        i = a

    # let m = j / 2. If i < m, max_cycle_length(i, j) = max_cycle_length(m, j)
    if (i < (j >> 1)) :
        i = j >> 1
    
    # to be able to compute j itself
    j += 1

    for x in range(i, j) :
        current_Val = x

        if (array[x] != 0) :
            cycle = array[x]
        else :
            while current_Val > 1 :

                if (current_Val % 2) == 0 :
                    current_Val = (current_Val >> 1)
                else :
                    #this does (3n + 1) AND divides by 2
                    current_Val =  current_Val + (current_Val >> 1) + 1
                    cycle += 1

                cycle += 1

            array[x] = cycle

        if cycle > max_cycle :
            max_cycle = cycle

        cycle = 1

    assert max_cycle > 0
    return max_cycle   

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :  
    """
    print three ints
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    while True :  
        a = collatz_read(r)
        if not a :
            return
        i, j = a  
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)

collatz_solve(sys.stdin, sys.stdout)