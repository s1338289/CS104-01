Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Average of 3 test
>>> 
============== RESTART: /Users/victordavidson/Documents/average.py =============
How many test scores would you like to average? 3
Enter test score: 50
Traceback (most recent call last):
  File "/Users/victordavidson/Documents/average.py", line 9, in <module>
    total = total+testScore
NameError: name 'total' is not defined. Did you mean: 'Total'?
>>> 
============== RESTART: /Users/victordavidson/Documents/average.py =============
How many test scores would you like to average? 
Traceback (most recent call last):
  File "/Users/victordavidson/Documents/average.py", line 5, in <module>
    howMany = int(input("How many test scores would you like to average? "))
ValueError: invalid literal for int() with base 10: ''
>>> 
============== RESTART: /Users/victordavidson/Documents/average.py =============
How many test scores would you like to average? 3
Enter test score: 50
Enter test score: 60
Enter test score: 70
The average for the test scores you entered is:  60.0
