# Authors: Amulya Badineni, Alioune Gueye, Michael Mongelli
# Filename: main.py
# Description: The program implements the ID3 decision tree learning algorithm.

import sys

if __name__ == '__main__':
    
    from info_gain import *
    from DecisionTree import *

    # ensure commmand line arguments are correct format, handle incorrect number of arguments
    if len(sys.argv) != 3:
        exit(
        "You must provide first the name of the input file and then the name of the output file. " +
        f"You only provided an input file '{sys.argv[1]}'"
        )

    # get input and output files from command line
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]

    # First in-class Entropy example
    testset = [({}, "Yes") for i in range(9)] + [({}, "No") for i in range(5)]
    print("First in-class entropy calculation:")
    print(f"\t{Entropy(testset)}") # print out entropy calculation

    # In-class IG examples
    S,_,_ = get_training_data("PlayTennisSampleDataFormat.txt")
    print("\nTask 1:")
    print("In-class information gain calculations (using 'PlayTennisSampleDataFormat.txt'):")
    for A in Values(S):
        # print out each information gain
        print(f"\t{A}: {format(IG(S,A), '.3f')}")

    # Task 1 - ID3 algorithm
    def ID3(examples, target_attr, attributes):
        # inputs:
        # examples: set of training examples, a list of tuples of the form ({example}, training_value)
        # target_attr: attr whose value is predicted by the tree
        # attributes: list of other attributes that may be tested by the learned Decision Tree

        # output: the root node of a learned decision tree

        root = DecTree() # initialize tree

        # if all examples are positive
        if all(training_value=="Yes" for (example, training_value) in examples): return DecTree("Yes")

        # if all examples are negative
        if all(training_value=="No" for (example, training_value) in examples): return DecTree("No")
            
        target_attr_vals = [training_value for (example, training_value) in examples] # values of target_attr in examples
        most_common_val = max(target_attr_vals, key=target_attr_vals.count) # most common value of target_attr
        if attributes == []: 
            # if attribute is empty, return node with most common value of target attr
            return DecTree(most_common_val)
        
        gains = { attr: IG(examples, attr) for attr in attributes } # compute IG of each possible attr for next node
        A = max(gains, key=gains.get) # get attribute that had the max info gain (the one that best classfies examples)
        root = DecTree(A, Values(examples)[A]) #set root of DecTree as A

        attributes.remove(A) # remove A from attributes now that it is in the tree

        for v in Values(examples)[A]:
            # create a subset of examples that have value v for A
            examples_v = [(example, training_value) for (example, training_value) in examples if example[A]==v]

            if examples_v == []:
                root.add_node(v, most_common_val) # add a leaf node with most common value of target_attr in examples
            else:
                root.values[v] = ID3(examples_v, target_attr, attributes) # add the subtree ID3 below new branch
                
        return root

    # Task 2 - learn tree from PlayTennis examples
    examples, target_attr, attributes = get_training_data(inputfile) # get data from input file to run ID3 on
    DT = ID3(examples, target_attr, attributes) # run the ID3 algorithm on the input
    print(target_attr+':\n')
    print(DT)

    # print results to output file specified on command line
    with open(outputfile, 'w') as f:
        print(target_attr+':\n', file=f)
        print(DT, file=f)

