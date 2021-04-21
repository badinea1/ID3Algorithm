def get_training_data(filename):
    # input name of CSV file containing training data
    # note: first line of file must be column names
    with open(filename,"r") as f:
        training_data = []
        from csv import DictReader
        for example in DictReader(f): # each line is saved into a dict
            # get enjoy_sport value from example
            example.pop("ExampleID") # remove unnecessary column
            training_value = example.pop(list(example.keys())[-1]) # get training value of example
            training_data.append((example, training_value)) # append pair to list of training examples

    # output list of training examples
    # where each example looks like: ({attributes}, enjoy_sport)
    # attributes is a dict, enjoy_sport is a string "yes" or "no"
    return training_data

def Entropy(S):
    # S is the set of training examples

    def log_2(p): 
        from math import log
        return 0 if p==0 else log(p, 2) # log_2(0) is defined as 0 for the Entropy function

    c = ["Yes", "No"] # classification of example as pos or neg

    # subset of S belonging to class i
    def S_(i): return [example for (example, training_value) in S if training_value==i]

    proportions = [len(S_(i))/len(S) for i in c] # proportions of favorable (pos ex's) and unfavorable (neg ex's) outcomes
    entropy = sum( -p * log_2(p) for p in proportions ) # sum the calculations performed on the proportions
    return entropy

def Values(S):
    # input: S is the set of training examples
    # output: dict of attributes and their possible values given the set S: {attr1: [possible values], attr2...} 

    values = {}
    for (example, training_value) in S:
        for A in example:
            if A in values: values[A].append(example[A]) # add value from example to list of values
            else: values[A] = [example[A]] # initialize list of values of attr A if it doesnt already exist

    for A in values:
        # a set only holds unique elements
        # thus values[A] now only holds unique possible values of attribute A
        values[A] = set(values[A])

    return values

def IG(S, A):
    # S is the set of training examples
    # A is an attribute of the data you would like to compute the information gain of

    # subset of S where attribute A has value v
    def S_(v): return [(example, training_value) for (example, training_value) in S if example[A]==v]

    ig = Entropy(S) - sum( (len(S_(v))/len(S)) * Entropy(S_(v)) for v in Values(S)[A] )
    return ig