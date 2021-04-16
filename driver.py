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

DT = Node(attribute="Outlook", values=["Sunny","Overcast","Rain"])

DT.set_child("Sunny", Node("Temperature", ["Hot","Mild","Cool"]))

# set child like this
#DT.get_child("Sunny").set_child("Hot", Node("Yes"))

# or like this
sunny = DT.get_child("Sunny")
sunny.set_child("Hot", Node("Yes"))

print(DT)