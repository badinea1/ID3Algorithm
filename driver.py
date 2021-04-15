from info_gain import *
from decisiontree import *

# First in-class Entropy example
test = [{"PlayTennis":"Yes"} for i in range(9)] + [{"PlayTennis":"No"} for i in range(5)]
print("First in-class entropy calculation:", Entropy(test))

# In-class Information Gain PlayTennis example
S = get_training_data("PlayTennisSampleDataFormat.txt")
for A in Values:
    if A != "PlayTennis": print(f"{A}: {format(IG(S,A), '.3f')}")

# initialize empty tree
dt = DecisionTree()
print('\n\n' + str(dt))

# add attribute Outlook as root node,
# its 3 possible values are the branches
dt.add_node({"Outlook": ["Sunny","Overcast","Rain"]}) 
print('\n\n' + str(dt))

# add Humidity as new node at the end of the Sunny branch,
# the new branches stemming from the Humidity branch are its possible values
dt.branches["Sunny"].add_node({"Humidity": ["Normal","High"]})
print('\n\n' + str(dt))

# same process again, adding Wind as new node
dt.branches["Sunny"].branches["Normal"].add_node({"Wind": ["Weak","Strong"]})
print('\n\n' + str(dt))

# add leaf nodes to the ends of the branches,
# the final attributes 'Yes' and 'No' have no possible values, so they terminate the branch
dt.branches["Sunny"].branches["Normal"].branches["Weak"].add_node({"Yes": []})
dt.branches["Sunny"].branches["Normal"].branches["Strong"].add_node({"No": []})
print('\n\n' + str(dt))