#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % coverage3 run --branch TestCollatz.py

To obtain coverage of the test:
    % coverage3 report -m
"""

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r    = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        r    = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        collatz_read(r)
        i, j = collatz_read(r)
        self.assertEqual(i,  100)
        self.assertEqual(j, 200)

    def test_read_3 (self) :
        r    = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        collatz_read(r)
        collatz_read(r)
        collatz_read(r)
        i, j = collatz_read(r)
        self.assertEqual(i,  900)
        self.assertEqual(j, 1000)

    def test_read_4 (self) :
        r = StringIO("")
        i = collatz_read(r)
        self.assertEqual(i, [])


    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5 (self) :
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)

    def test_eval_6 (self) :
        v = collatz_eval(10,10)
        self.assertEqual(v, 7)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("1 10\n100 200\n201 210\n1000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n1000 900 174\n")


# ----
# main
# ----

main()

"""
% coverage3 run --branch TestCollatz.py
FFFFFF.....FF
======================================================================
FAIL: test_eval_1 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 69, in test_eval_1
    self.assertEqual(v, 20)
AssertionError: 1 != 20

======================================================================
FAIL: test_eval_2 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 73, in test_eval_2
    self.assertEqual(v, 125)
AssertionError: 1 != 125

======================================================================
FAIL: test_eval_3 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 77, in test_eval_3
    self.assertEqual(v, 89)
AssertionError: 1 != 89

======================================================================
FAIL: test_eval_4 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 81, in test_eval_4
    self.assertEqual(v, 174)
AssertionError: 1 != 174

======================================================================
FAIL: test_eval_5 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 85, in test_eval_5
    self.assertEqual(v, 174)
AssertionError: 1 != 174

======================================================================
FAIL: test_eval_6 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 89, in test_eval_6
    self.assertEqual(v, 7)
AssertionError: 1 != 7

======================================================================
FAIL: test_solve_1 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 108, in test_solve_1
    self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
AssertionError: '1 10 1\n100 200 1\n201 210 1\n900 1000 1\n' != '1 10 20\n100 200 125\n201 210 89\n900 1000 174\n'
- 1 10 1
?      ^
+ 1 10 20
?      ^^
- 100 200 1
+ 100 200 125
?          ++
- 201 210 1
?         ^
+ 201 210 89
?         ^^
- 900 1000 1
+ 900 1000 174
?           ++


======================================================================
FAIL: test_solve_2 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 114, in test_solve_2
    self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n1000 900 174\n")
AssertionError: '1 10 1\n100 200 1\n201 210 1\n1000 900 1\n' != '1 10 20\n100 200 125\n201 210 89\n1000 900 174\n'
- 1 10 1
?      ^
+ 1 10 20
?      ^^
- 100 200 1
+ 100 200 125
?          ++
- 201 210 1
?         ^
+ 201 210 89
?         ^^
- 1000 900 1
+ 1000 900 174
?           ++


----------------------------------------------------------------------
Ran 13 tests in 0.004s

FAILED (failures=8)







% coverage3 report -m
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          23      0      6      0   100%   
TestCollatz      62      1      0      0    98%   123
---------------------------------------------------------
TOTAL            85      1      6      0    99%   

"""
