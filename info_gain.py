from values import Values

def get_training_data(filename):
    # input name of CSV file containing training data
    # note: first line of file must be column names
    with open(filename,"r") as f:
        training_data = []
        from csv import DictReader
        for example in DictReader(f): # each line is saved into a dict
            # get enjoy_sport value from example
            example.pop("ExampleID") # remove unnecessary column
            training_data.append(example) # append pair to list of training examples

    # output list of training examples
    # where each example looks like: ({attributes}, enjoy_sport)
    # attributes is a dict, enjoy_sport is a string "yes" or "no"
    return training_data

def Entropy(S):
    # S is the set of training examples

    def log_2(p): 
        from math import log
        # log_2(0) is defined as 0 for the Entropy function
        return 0 if p==0 else log(p, 2)

    c = Values["PlayTennis"]

    # subset of S belonging to class i
    def S_(i): return [example for example in S if example["PlayTennis"]==i]

    proportions = [len(S_(i))/len(S) for i in c] # proportions of S that belong to each class i in c
    entropy = sum( -p * log_2(p) for p in proportions ) # sum the calculations performed on the proportions
    return entropy

def IG(S, A):
    # S is the set of training examples
    # A is an attribute of the data you would like to compute the information gain of
    
    # subset of S where attribute A has value v
    def S_(v): return [example for example in S if example[A]==v]

    ig = Entropy(S) - sum( (len(S_(v))/len(S)) * Entropy(S_(v)) for v in Values[A] )
    return ig