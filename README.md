The program is a function taking a function and returning a function.

Input
=====
List of integers on foldr form (TODO is other structures possible as input?)

Example input
-------------
\c.\n.(c 0 (c 1 (c 2 (c 3 n))))
  where 0 = \f.\x.x
        1 = \f.\x.(f x)
        2 = \f.\x.(f (f x))
        3 = \f.\x.(f (f (f x)))


Output
======
TODO: does the outputed structure need to be extensionally or intentionally equivalent with the intended outputed function

Paper
=====
http://www.mathstat.dal.ca/~selinger/papers/lambdanotes.pdf
