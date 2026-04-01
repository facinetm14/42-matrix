# Matrix

Python implementation of the 42 project "Enter the Matrix", an introduction to linear algebra through small, focused exercises on vectors, matrices, and fundamental operations.

## Project Goal

The purpose of this project is to build intuition for linear algebra by implementing the core operations manually instead of relying on numerical libraries. The subject emphasizes understanding what vectors and matrices represent, how linear operations behave, and how these ideas connect to fields such as graphics, simulation, and data science.

In practice, the project asks you to:

- model vectors and matrices with generic types
- implement basic algebraic operations from scratch
- test each exercise with a runnable `main`
- respect the algorithmic constraints (time and space complexity) given in the subject

## Subject Context

According to the provided subject, this module is meant as a hands-on introduction to:

- vector spaces
- linear maps
- matrix representations
- computational reasoning around time and space complexity

The general rules also state that:

- generic types are required
- first-class functions must be supported by the chosen language
- operator overloading is optional
- mathematical libraries must not be used unless explicitly authorized

This repository uses Python with generic type hints to stay close to those expectations while keeping the code easy to read and iterate on.

## Repository Structure

```text
.
├── Makefile
├── requirement.txt
└── src
    ├── ex00
    │   ├── Matrix.py
    │   ├── Vector.py
    │   └── main.py
    ├── ex01
    │   ├── linear_combination.py
    │   └── main.py
    └── ex02
        ├── linear_interpolation.py
        └── main.py
    ...
```

## Exercises

- Exercise 00: Add, Subtract and Scale Matrix or Vector
- Exercise 01: Linear Combination
- Exercise 02: Linear Interpolation (lerp)

## Setup

Setup project environment with

```bash
make setup
```

## Running the Exercises

Run each exercise entry point with the `make ex<exercice number>`:

```bash
make ex00
```
