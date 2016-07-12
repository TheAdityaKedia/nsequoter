nsequoter Documentation
=======================

:Author: Aditya Keida
:Version: 1.0.0
:Date: 7th Jul, 2016
:License: MIT

.. contents::


   

Motivation
----------

Python is fast becoming the programing language of choice for Quants 
and Data Analysts, and an easy way to fetch data from the most 
important sources is needed. The power and popularity of Python reside 
in the ability to reuse code on through over 40000 libraries and modules. 
That said, getting quotes from the National Stock Exchange of India (NSE) 
is quite hard in python, and most other languages for that matter.

nsequoter is a module that aims to make it trivially easy to get these 
quotes from the NSE, by simply reading the data off the exchange's website
http://www.nseindia.com and importing it into python. The current version 
Supports equity and equity futures. equity options and currency derivatives 
will be added in the next version. Indexes will follow after that.

Usage
-----
The simplest way to use the library is as follows::

  >>import nsequoter #imports the module and all the functions in it

  >>#to get a float value of the quote for '3M India'
  >>nsequoter.get_equity_quote('3MINDIA') #use the listed symbol as argument

  >>#to get a float value of the quote for '3M India' July futures
  >>nsequoter.get_futures_quote('3MINDIA', 'JUL') #use symbol and month as argument
	
Note that the arguments are not case sensitive. However, the symbol/code
should be as listed. Months can be entered as three letter months (String)
or their calendar number (Jul = 7, Aug = 8, etc.)

Futures contracts expire on the Thursday of each month. Queries after
that date will result in an exception.
