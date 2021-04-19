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

    root = DecTree("Outlook", ["Sunny","Overcast","Rain"])
    root.add_node("Rain", "Wind", ["Weak","Strong"])
    
    