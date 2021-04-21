# ID3Algorithm
# CSC 426 Project 3: Decision Tree Implementation, Experiments, and Analysis
# Authors: Amulya Badineni, Alioune Gueye, Michael Mongelli
# Filename: README.md
# Description: Describes the contents of the submission.

This repository contains a Python based Decision Tree Implementation.

## Contents
The repository includes four main deliverables:
  1. **D2**: the verification that your program works correctly for the example data provided in class for the PlayTennis task.
  2. **D3**: the decision tree that your program learns for the four EnjoySport training examples + a write-up containing answers to the questions for Task 3
  3. **main.py, info_gain.py, DecisionTree.py**: our source code
  4. **Reflection**: a writeup that addresses the following:
       1. anything positive we enjoyed or learned from this assignment,
       2. anything negative we didn't like about this assignment,
       3. any parts of this assignment we found easy,
       4. any parts of this assignment we found challenging or couldn't get working correctly,
       5. Details on how our team functioned
     
**NOTE**: For the program to run successfully, you must have input and output file locations as command line arguments (shown below). 

**NOTE**: Data in input file must have data in a comma separate value (csv) format. 

**LINK TO REPO**: https://github.com/badinea1/ID3Algorithm

## Build Instructions for the HPC
1. Method 1: Cloning repository

```
module add python
git clone https://github.com/badinea1/ID3Algorithm.git
python main.py inputDataFileLocation outputFileLocation

```

2. Method 2: 
On OnDemand, go to your File Home Directory and upload source code and the input files. Then, in the HPC terminal, enter: 

``` 
   module add python
   python main.py inputDataFileLocation outputFileLocation
```
