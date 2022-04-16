# Homework 8.5: Unit Testing
In this assignment, you'll be practicing two of the trickier skills of unit testing: mocking database calls, and finding good parts of your code to test. Any points you receive here will be applied to your lowest individual project milestone grade.

As always, turn in your work by creating a GitHub repo in the class org named `hw8.5-<your_campus_id>`, and then turning that in on Gradescope.

To start, copy down all of the files in this repo except the README into your working directory.


**1. (1 point) Warmup:** We'll warm up by writing tests for an existing function. Take a look at the function in `parentheses.py` and write unit tests for at least two test cases for it in a file called `parentheses_tests.py`. The function is returning the number of parentheses that would have to be removed to balance the input string. Try to come up with some interesting edge cases!. 

**2. (2 points) Choose your own units:** Writing tests is relatively easy when ready-made functions are handed to you to test. In the real world, it's your job to write modular code that has small, testable parts. Instead of testing the code in `messy_function.py` directly, abstract out some of the logic into its own function(s) and write at least two unit tests for those! Do so in a file called `modular_tests.py`.

**3. (2 points) DB mocking:** Consider the function in `database.py`. If we wanted to test it, we would have to use mocking to ensure that actual reads and writes are not made to our DB. In a file called `database_tests.py`, write a unit test for this function by mocking out the database and replacing it with a list of `Rating` objects.

*Hint 1:* You will have to mock out multiple attributes of the `db`, as `db.session.commit()` and `db.session.delete()` are both called. Additionally, you'll have to mock the `Ratings` class so that its `query.all()` attribute returns... something else.

*Hint 2*: What might that "something else" be? There are a lot of ways to do this, but a common approach is to have your test class have a "database" -- which is really just a list of DB model objects -- as an instance variable, and to access that list in all your mocked calls.