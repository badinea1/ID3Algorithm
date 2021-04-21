# Authors: Amulya Badineni, Alioune Gueye, Michael Mongelli
# Filename: main.py
# Description: The program creates a tic tac toe learning system that improves with experience.

import sys

if __name__ == '__main__':
    
    from info_gain import *
    from DecisionTree import *

    if len(sys.argv) != 3:
        exit(
        "You must provide first the name of the input file and then the name of the output file. " +
        f"You only provided an input file '{sys.argv[1]}'"
        )

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]

    # First in-class Entropy example
    testset = [({}, "Yes") for i in range(9)] + [({}, "No") for i in range(5)]
    print("First in-class entropy calculation:")
    print(f"\t{Entropy(testset)}")

    # In-class Information Gain PlayTennis example
    S = get_training_data("PlayTennisSampleDataFormat.txt")
    print("In-class information gain calculations (using 'PlayTennisSampleDataFormat.txt'):")
    for A in Values(S):
        print(f"\t{A}: {format(IG(S,A), '.3f')}")

    #initialize an array to hold the get_training_data
    examples = get_training_data(inputfile)

    #get all the attributes that are not the one i'm trying to predict (so not PlayTennis)

    # ID3 algorithm
    def ID3(examples, target_attr, attributes):
        # inputs:
        # examples: set of training examples, a list of tuples of the form ({example}, training_value)
        # target_attr: attr whose value is predicted by the tree
        # attributes: list of other attributes that may be tested by the learned Decision Tree

        # output: the root node of a learned decision tree

        root = DecTree() # initialize tree

        count_pos = 0 # count for the positive examples in training data
        count_neg = 0 # count for the negative examples in training data

        target_A = "yes" # holds the most common value of Target_Attr in examples

        # iterate through examples
        for i in examples:

            if i.get(target_attr) == "Yes": # count the number of positive examples
                count_pos += 1
            elif i.get(target_attr) == "No": # count the number of negative examples
                count_neg += 1 
            
        if count_pos == len(examples): # if all examples are positive
            return DecTree("Yes")
        elif count_neg == len(examples): # if all examples are negative
            return DecTree("No")
            
        # check if attributes is empty
        if attributes == []:
            if count_pos > count_neg: # label node with the most common value of target_Atrr based on count
                return DecTree("Yes")
            elif count_neg > count_pos:
                return DecTree("No")
            elif count_pos == count_neg: #what is the yes and no equal each other
                return DecTree("Yes")

        # update target_A to hold the most common value of target_Attr
        if count_pos > count_neg:
            target_A = "Yes"
        elif count_neg > count_pos:
            target_A = "No"
        
        gains = {A:IG(S,A) for A in attributes} # compute IG of each possible attr for next node
        A = max(gains, key=gains.get) #get attribute that had the max info gain (the one that best classfies examples)
        root = DecTree(A, Values[A]) #set root of DecTree as A

        attributes.remove(A) # 
        for v in Values.get(A):
            examples_vi = [] # create a subset of examples that have values v_i for A

            #Let examples{vi} be the subset of Examples that have values vi for A;
            for e in examples:
                if e.get(A) == v:
                    examples_vi.append(e) # append to subset

            if examples_vi == []: # check if examples{v_i} is empty
                root.add_node(v, TA) # add a leaf node with label = most common value of target _Attr in examples
            else:
                root.values[v] = ID3(examples_vi, target_attr, attributes) # add the subtree ID3 below new branch
                
                #new_node = ID3(examples_v, target_attr, attributes)
                #root.add_node(v, new_node.attr, new_node.values.keys())
                #root.add_node(v, )
        
        print(root) # print tree
        return root

    ID3(examples, "PlayTennis", ["Outlook", "Temperature", "Humidity", "Wind"]) # call function
