## University of Toronto Python Exercises

This is where I will be uploading any Python3 exercises during my time at U of T, where I am currently sitting in on CS108 as well as taking the online Coursera course in order to take part in online exercises.

I'll still be working on my primary Ruby projects when I find time, but for now it is pretty imperative that I take the time to learn the ins and outs of coding at a University level. Good luck, me!

### Exercise 3.1

```html

  Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
  Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked
  above 40 hours.

  Use 45 hours and a rate of 10.50 per hour to test the program (the pay should
  be 498.75). You should use input to read a string and float() to convert the string to a number.
  Do not worry about error checking the user input - assume the user types numbers properly.

```

Started out easy enough, the math I could do in my head or on paper - but figuring out how to write it as code gave me more of a challenge. At first I assumed it would be something to do with remainders (%) but quickly figured out that the best solution is often the simplest one (h - 40).

**What I Learned:**
Constants are important! The number 40 never changes, and it's not always a bad thing to just put a number into your code that isn't a variable - which was the last step for me in figuring out this exercise.

### Exercise 3.3

```html

  Write a program to prompt for a score between 0.0 and 1.0. If the score
  is out of range, print an error. If the score is between 0.0 and 1.0, print a
  grade using the following table:

  Score Grade
  >= 0.9 A
  >= 0.8 B
  >= 0.7 C
  >= 0.6 D
  < 0.6 F

  If the user enters a value out of range, print a suitable error
  message and exit. For the test, enter a score of 0.85.

```

This one was a lot easier to figure out than 3.1 - just takes a bit of shuffling the lines around.

**What I Learned:**
The importance of code hierarchy in order to allow every possible input between 0.0 and 1.0 to pass through the code, as well as where to place tests for invalid inputs. Seems like simple stuff but even the simple stuff is important practice. I mean ... it's all pretty important I guess.  

### Exercise 4.6

```html

  Write a program to prompt the user for hours and rate per hour using input
  to compute gross pay. Award time-and-a-half for the hourly rate for all hours
  worked above 40 hours. Put the logic to do the computation of time-and-a-half
  in a function called computepay() and use the function to do the computation.

```

A continuation of exercise 3.1 that calls a function to eliminate repetitive code, using the _return_ statement to store a value.

**What I Learned:**

Return statements seem to be the beginning of a more complex programming, where the user is given back a value that can be used later. Rather than simply doing something like _print()_ and moving on, we're now working with functions that can make a returned value more valuable.

I'm also finding it harder to code on Sundays when the Broncos are __this__ good at football.

(_Go Broncos..._)

### Exercise 5.2

```html

Write a program that repeatedly prompts a user for integer numbers until the
user enters 'done'. Once 'done' is entered, print out the largest and smallest
of the numbers. If the user enters anything other than a valid number catch it
with a try/except and put out an appropriate message and ignore the number.
Enter 7, 2, bob, 10, and 4 and match the output below.

```

The first exercise to use an indefinite loop until the user breaks the code by typing "done", as well as the first exercise using the Boolean data type.

**What I Learned:**

Today I learned that there are different types of flags for different types of input! Depending on the type of data that you are expecting.

Also, even though the course has yet to cover _and_ statements, I knew in my heartiest of hearts that it would be the most efficient way of writing lines 14-16:

```Python3
elif largest is None and smallest is None:
      largest = num
      smallest = num
```

Rather than writing out separate lines of code to check both "largest" and "smallest" for a value, the 14th line of code will only run once - as it's given the first value inputted - assigning the first integer given to both "largest" and "smallest" all in one go. Neato.

### Exercise 6.5

```html

Write code using find() and string slicing (see section 6.10) to extract
the number at the end of the line below. Convert the extracted value to a
floating point number and print it out.

```

Our first exercise using string slicing to capture a small portion of a long string, and converting that data. A very simple exercise, I'm looking forward to learning more intelligent ways of slicing using conditional statements.

**What I Learned:**

As someone with a huge interest in communication technology, being able to slice a string and collect useful segments of information within a piece of data is a very exciting first step.

Large streaming applications - Twitch and more recently YouTube Gaming for example - have always fascinated me with complex live-chat, and appear to use a lot of the same functions covered in chapter six. Very excited to dive into this week's material.

### Exercise 7.1

```html

Write a program that prompts for a file name, then opens that file and reads
through the file, and print the contents of the file in upper case. Use the
file words.txt to produce the output below.

```

Our first exercise for opening & reading .txt files, in order to run a couple functions that do something simple with the data.

**What I Learned:**

Today I learned how to read() a file, turning all of the data into one continuous string that can then be passed through a block of code. I've also learned quite a bit today about the semantics of opening .txt files and how to search using a for loop.

### Exercise 7.2

```html

Write a program that prompts for a file name, then opens that file and reads
through the file, looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name.

```

A more complex continuation of opening & reading files, this time finding the 'average spam confidence' within the .txt file.

**What I Learned:**

As this exercise grew more complicated with more variables, I started to notice the importance of having efficient variable names - as the lines of code become more and more complex with new values.

### Exercise 8.4

```html

Open the file romeo.txt and read it line by line. For each line, split the line
into a list of words using the split() method. The program should build a list
of words. For each word on each line check to see if the word is already in the
list and if not append it to the list. When the program completes, sort and
print the resulting words in alphabetical order.

```

### Exercise 8.5

```html

Open the file mbox-short.txt and read it line by line. When you find a line that
 starts with 'From ' like the following line:

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

You will parse the From line using split() and print out the second word in the
line (i.e. the entire address of the person who sent the message). Then print
out a count at the end. Hint: make sure not to include the lines that start
with 'From:'.

```
