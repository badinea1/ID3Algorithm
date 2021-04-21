import sys


if __name__ == '__main__':
    
    from info_gain import *
    from DecisionTree import *

    # total arguments
    n = len(sys.argv)
    print("Total arguments passed:", n)

    # First in-class Entropy example
    test = [{"PlayTennis":"Yes"} for i in range(9)] + [{"PlayTennis":"No"} for i in range(5)]
    print("First in-class entropy calculation:")
    print(f"\t{Entropy(test)}")

    # In-class Information Gain PlayTennis example
    #S = get_training_data("PlayTennisSampleDataFormat.txt")
    S = get_training_data(sys.argv[1])
    print("In-class information gain calculations:")
    for A in Values:
        if A != "PlayTennis": print(f"\t{A}: {format(IG(S,A), '.3f')}")

    #initialize an array to hold the get_training_data
    examples = get_training_data(sys.argv[1])

    #print(examples)

    #get all the attributes that are not the one i'm trying to predict (so not PlayTennis)

    #ID3()

    # ID3 algorithm
    def ID3(examples, target_attr, attributes):

        # examples are the training examples
        # target_attr is the attribute whose value is predicted by the tree
        # attributes is a list of other attributes that may be tested by the learned DT

        # returns by the learned dt

        root = DecTree() # initialize tree

        # compute IG of each possible attr for next node
        #gains = {A:IG(S,A) for A in Values if A not in DecTree.attrs and A != "PlayTennis"}

        #if gains=={}: 
            # if there are no more attrs to measure the gains of, the tree is complete, end alg
        #    print(root)
        #    return

        #print(root)
        #output_file = open(sys.argv[2], 'w')
        #output_file.write = (print(root))
        #output_file.close()

        count_pos = 0
        count_neg = 0

        TA = "yes"

        #examples[i] #gives me the ith dictionary

        #examples[i][target_attr] #will give me the yes or no

        #If all Examples are positive, return single-node tree Root, with label = + (pos)
        for i in examples:

            if i.get(target_attr) == "Yes":
                count_pos += 1
            elif i.get(target_attr) == "No":
                count_neg += 1 
            
        if count_pos == len(examples):
            return DecTree("Yes")
        elif count_neg == len(examples):
            return DecTree("No")

           #If Attributes is empty, return single-node tree Root, with label = the most common value of Target_Attr in Examples;
            
        # check if attributes is empty
        if attributes == []:
            if count_pos > count_neg:
                return DecTree("Yes")
            elif count_neg > count_pos:
                return DecTree("No")
            elif count_pos == count_neg: #what is the yes and no equal each other
                return DecTree("Yes")

        if count_pos > count_neg:
            TA = "yes"
        elif count_neg > count_pos:
            TA = "No"
        

        #// decision attribute for root is A
        gains = {A:IG(S,A) for A in attributes}
        A = max(gains, key=gains.get) #get attribute that had the max info gain
        root = DecTree(A, Values[A]) #set root of DecTree as A

        #print(gains)

            #you use info_gain
            # compute IG of each possible attr for next node
                #gains = {A:IG(S,A) for A in Attributes and A != "PlayTennis"}

            #figure out which attribubte gives me the max IG
            #A = attr from Attributes that best-classified Examples;

        
        values_A = []

        attributes.remove(A)
        for v in Values.get(A):
            examples_v = []

            for e in examples:
                if e.get(A) == v:
                    examples_v.append(e)

            #print(A)
            #print(attributes)
            #root.add_node(v, "yes")
            #values_A.append(v)


            if examples_v == []:
                root.add_node(v, TA)
            else:
                root.values[v] = ID3(examples_v, target_attr, attributes)
                #root.add_node(v, )
        
        print("GROOOT")
        print(root)
        return root

            #add a new tree branch below Root, corresponding to the test A = vi; !!!!!!!!

            #Let examples{vi} be the subset of Examples that have values vi for A;

            #If Examples{v_i} is empty {
                #below the new branch add a leaf node with label = most common value of target _Attr in examples;
            #} else {
                #below the new branch add the subtree ID3 (examples_ {vi}, Target_Attr, Attributes - {A}); !!!!!!!
                #call the function
            #}
        #} // end for loop

        #return Root;

    #del values["PlayTennis"]
    ID3(examples, "PlayTennis", ["Outlook", "Temperature", "Humidity", "Wind"])
