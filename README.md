## Exercises

### Task 1: Program calculate year of birth! 
Create a program that calculates the year of birth.
- First part:
    - define the variables `age` and `name`
    - make a calculation for the year in which the person was born
    - print out "OMG <person>, you are <age> years old, so you were born in <year>" with the correct values

- Second Part:
    - prompt the user for input and re-assigning the variable `age` and `name`
    - figure out a way to account for if the persons' birthday has already happened this year or not

- Extra
    - go look into the library time
    - print out the amount of hour this person has lived

### Task 2: Lists - Restaurant Waiter Helper program
- To make a program that helps a waiter with his menu and his orders.
- User Stories
    1. As a User I want to be able to see the menu in a formatted way, so that I can order my meal.

    2. As a User I want to be able to order 3 times, and have my responses added to a list, so they aren't forgotten

    3. As a user, I want to have my order read back to me in formatted way, so I know what I ordered.
    
### Task 3:Xmas Holiday List that never ends!

- User stories:
    1. As a user, I want to be able to add items to the list, so I can read it later.

    2. As a user, I want to be able to keep adding things to the list until I use exit

    3. As a user, I should be able to use the word exit in a sentence and still have the program terminate, so that anyone can use it

    4. as a user, when the program exits, I want to see the complete list in caps lock and numbered, so that I know what to buy. example:


### Task 4: Fizz Buzz!

- Core:
    - Write a program that prints the numbers from 1 to 100.
    - For multiples of three print "Fizz" instead of the number
    - For the multiples of five print "Buzz" instead of the number
    - For numbers which are multiples of both three and five print "FizzBuzz".

- Extra:
    - make a new fizzbuzz file and make it functional
    - make it, so we can decide which numbers to substitute for fizz and buzz using functions

### Task 5: Functional Calculator

- Complete the core tasks
- Core 1: build function containing
    - add,
    - subtract,
    - multiply,
    - divide.

- Core 2: Build more functions for
    - area of a circle
    - area of a square
    - area of a triangle (just find the easiest way)

- Extra:
    - run the function with arguments
    - assert against known values - so adding 10 + 30 will always be 40
    
### Task 6: Loops and lists

- make a loop with a range that says hello 10 times
- create another loop with a range that asks for names and appends to list_names
- make a loop that iterated over each name in list_names and format's it into lowercase in a new variable called list_names_lower
- Iterate over the list of values to find if they are even
 
## OOP Exercises

### Task 1: Fizzbuzz class
The Problem
"Write a program that prints the numbers from 1 to 100.
But, for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”."

### Task 2: Scrabble word calculator
Base Scrabble word calculator instructions
Given the below scoring create a Scrabble word calculator that will provide the correct scores dependent on the string provided.
```
Letter                             Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
```
### Task 3: TDD Bread Factory! :bread:

- Timings:
60-90 Minutes

- Summary

TDD bread factory is the latest bread brand in Py Land. It always produces the best bread because it has the best testing strategy!
What they do is before they make any new bread, they make a test to make sure the end output is correct. Then they adjust the recipe until it's just right!
You are going to do the same with bread! This is called Test Driven Development.

- Tasks
This exercise is going to bring together lots of concepts.

### Task 4: Naan factory
To run the naan factory do the following:

```
import naan_factory
run_factory()
```


### TDD - test driven development

1. write the test
2. run it, and read the error
3. code and make it pass the test

this helps with:
- Stop over engineering
- Maintainable code
- Reduce technical debt
- Goes well with agile and working code
- errors can be your guide in complex systems

How it works is that we write unit tests.

##### Unit Tests

Test single pieces of code. Like a function.

**base of a test**
Usually has 3 phases.
- setup phase (know variables)
- calling of the function / piece of code with know variables
- asserting for expect output

- User stories for Naan Factory

1. As a user, I can use the make_dough with 'water' and 'flour' to make 'dough'.

2.As a user, I can use the bake_dough with dough to get naan.

3.As a user, I can use the run_factory with water and flour and get naan.



