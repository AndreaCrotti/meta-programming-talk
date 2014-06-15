================
Meta Programming
================

.. TODO: have a look at org-gcal for syncing things around
.. TODO: check why slime is not loading correctly

Twitter: @andreacrotti

Slides: https://github.com/AndreaCrotti/meta

Working for Depop

Agenda
======

- What is metaprogramming
- An historical perspective
- The real meta language
- Meta programming in Python

  + decorators
  + meta classes
  + macros (intro to the bytecode first?)


Metaprogramming
===============

A Lisp primer
=============

- why we show Lisp code
- explain the homoconoic thing

Lisp
====

.. In a homoiconic language the primary representation of programs is
   also a data structure in a primitive type of the language itself.

   Lisp in particular uses S-expressions as an external representation
   for data and code.  S-expressions can be read with the primitive
   Lisp function READ, which returns Lisp data: lists, symbols numbers
   and strings.

   Then EVAL computes side effects and return a result, and the result
   is printed by PRINT.

- very minimal syntax
- *homoiconocity*


.. code:: cl

    ((:name "john" :age 20) (:name "mary" :age 18))
    ;; 
    (* (sin 1.1) (cos 2.03))

.. In this case above here '* becomes a symbol, and 'sin as well
.. while the other values are just parsed as numbers as they are

Lisp Evaluation
===============

.. make a nice graph about the REPL loop
.. The real power of Lisp is that it's possible to simply write S-expressions
.. which are understood without the need of parsing them

- READ
- EVAL
- PRINT
- LOOP


Lisp macros
===========


Metaprogramming in Lisp
=======================

.. Thanks

Metaprogramming in Python
=========================

.. Is Python homoiconic?

- function decorators
- class decorators
- metaclasses
- why one and why the other? (implicit vs explicit)

Decorators
==========

Metaclasses
===========

Difference between Python2 and Python3? (maybe or maybe not)


Bibliography
============

.. _`what made lisp different`: http://www.paulgraham.com/diff.html
.. _`revenge of the nerds`: http://www.paulgraham.com/icad.html
.. _`homoiconity is not the point`: http://calculist.org/blog/2012/04/17/homoiconicity-isnt-the-point/
.. _`metaprogramming by examples`: http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example/
.. _`python decorators and lisp macros`: http://programmers.stackexchange.com/questions/213858/python-decorators-and-lisp-macros
.. _`metaprogramming answer`: http://stackoverflow.com/questions/2565572/metaprogramming-self-explanatory-code-tutorials-articles-books/2566561#2566561
