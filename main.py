if __name__ == '__main__':
    
    from info_gain import *
    from DecisionTree import *

    # First in-class Entropy example
    test = [{"PlayTennis":"Yes"} for i in range(9)] + [{"PlayTennis":"No"} for i in range(5)]
    print("First in-class entropy calculation:")
    print(f"\t{Entropy(test)}")

    # In-class Information Gain PlayTennis example
    S = get_training_data("PlayTennisSampleDataFormat.txt")
    print("In-class information gain calculations:")
    for A in Values:
        if A != "PlayTennis": print(f"\t{A}: {format(IG(S,A), '.3f')}")
'''
    # ID3 algorithm
    def ID3():
        root = DecTree() # initialize tree

        # compute IG of each possible attr for next node
        gains = {A:IG(S,A) for A in Values if A not in DecTree.attrs and A != "PlayTennis"}

        if gains=={}: 
            # if there are no more attrs to measure the gains of, the tree is complete, end alg
            print(root)
            return

        # get attribute that had the max info gain
        A = max(gains, key=gains.get)
        # 
        root = DecTree(A, Values[A])
        print(root)'''