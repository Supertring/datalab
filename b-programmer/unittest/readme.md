# Unit Testing
### What is Unit Testing?
* Smallest unit of code are tested
* White Box testing method is used

### Background

* test fixture:
  * A base for running unit test
  * Ensures necessary environments in which tests are run
    * Creating temporary database
    * Staring a server process
* test cases:
  * specific set of conditions designed to assess the functionality of a software application
* test suite:
  * collection of test cases grouped together for a specific purpose
* test runner:
  * is a component that set up the execution of tests and provides the outcome to the user

## Basic Terms:
* __asertEqual()__: Used to check if the result obtained is equal to the expected result
* __assertTrue()/assertFalse()__: Used to verify if a given statement is true or false
* __assertRaises()__: Statement is used to raise a specific exception