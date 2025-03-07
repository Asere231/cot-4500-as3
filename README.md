# COT-4500 Assignment 3

## Overview

This repository contains the implementation of numerical methods for solving differential equations as specified in Assignment 3a of COT-4500.

## Dependencies

- Python 3.8+
- NumPy

To install dependencies, run:

```bash
pip install -r requirements.txt
```

## Running the Main Script

To execute the main script, navigate to the 'src/main' directory and run:
(Note: use python or python3, depending on the version you have, in my case is python3!)

```bash
python3 assignment_3.py
```

## Running the Test Scripts

To execute the test script, navigate to the 'root' directory and run:
(Note: use python or python3, depending on the version you have, in my case is python3!)

```bash
python3 -m unittest src.test.test_assignment_3
```

## Functionality

The script implements the following numerical methods:

- Euler Method
- Runge-Kutta Method

These methods are used to solve the differential equation 't - y^2' over a specified range with a set number of iterations.

## Authors

Bryan Aneyro Hernandez
