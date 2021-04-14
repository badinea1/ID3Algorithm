import csv
from math import *

def get_training_data(filename):
    # input name of CSV file containing training data
    # note: first line of file must be column names
    with open(filename,"r") as f:
        training_data = []
        for example in csv.DictReader(f): # each line is saved into a dict
            # get enjoy_sport value from example
            example.pop("ExampleID") # remove unnecessary column
            training_data.append(example) # append pair to list of training examples

    # output list of training examples
    # where each example looks like: ({attributes}, enjoy_sport)
    # attributes is a dict, enjoy_sport is a string "yes" or "no"
    return training_data

# possible values of each attribute
Values = {
    "Outlook": ["Sunny","Overcast","Rain"],
    "Temperature": ["Hot","Mild","Cool"],
    "Humidity": ["Normal","High"],
    "Wind": ["Weak","Strong"],
    "PlayTennis": ["Yes","No"]
}

def Entropy(S):
    # S is the set of training examples

    c = Values["PlayTennis"]

    len_S = len(S) # total number of examples in S

    # partition S by classes i in c
    S = {i:[example for example in S if example["PlayTennis"]==i] for i in c}

    proportions = [len(S[i])/len_S for i in c] # proportions of S that belong to each class i in c
    return sum( -p * log(p, 2) if p!=0 else 0 for p in proportions )

def IG(S, A):
    # S is the set of training examples
    # A is an attribute of the data you would like to compute the IG of
    
    # get subset of examples in S where attribute A has value v
    def S_(v): return [example for example in S if example[A]==v]

    return Entropy(S) - sum( (len(S_(v))/len(S)) * Entropy(S_(v)) for v in Values[A] )

# First in-class Entropy example
#test = [{"PlayTennis":"Yes"} for i in range(9)] + [{"PlayTennis":"No"} for i in range(5)]
#print(Entropy(test))

# In-class PlayTennis example
S = get_training_data("PlayTennisSampleDataFormat.txt")
for A in Values:
    if A != "PlayTennis": print(f"{A}: {format(IG(S,A), '.3f')}")