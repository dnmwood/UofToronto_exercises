## University of Toronto Python Exercises

This is where I will be uploading any Python3 exercises during my time at U of T, where I am currently sitting in on CS108 as well as taking the online Coursera course in order to take part in online exercises.

I'll still be working on my primary Ruby projects when I find time, but for now it is pretty imperative that I take the time to learn the ins and outs of coding at a University level. Good luck, me!

### Exercise 3.1

```html
  <p>
  Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
  <p>
```

Started out easy enough, the math I could do in my head or on paper - but figuring out how to write it as code gave me more of a challenge. At first I assumed it would be something to do with remainders (%) but quickly figured out that the best solution is often the simplest one (h - 40).

**What I Learned:**
Constants are important! The number 40 never changes, and it's not always a bad thing to just put a number into your code that isn't a variable - which was the last step for me in figuring out this exercise.

### Exercise 3.3

```html
  <p>
  Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:

  Score Grade
  >= 0.9 A
  >= 0.8 B
  >= 0.7 C
  >= 0.6 D
  < 0.6 F

  If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
  </p>
```

This one was a lot easier to figure out than 3.1 - just takes a bit of shuffling the lines around.

**What I Learned:**
The importance of code hierarchy in order to allow every possible input between 0.0 and 1.0 to pass through the code, as well as where to place tests for invalid inputs. Seems like simple stuff but even the simple stuff is important practice. I mean ... it's all pretty important I guess.  
