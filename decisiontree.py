'''
Notes:

create a new tree:
    dt = DecisionTree() 
    this creates tree with a single empty node (attr=? and has no values i.e. no branches)

add a first node (root):
    node = {attr1 : [val1,val2,val3]}
    dt.add_node(node)

so now the tree looks like:
    attr1
      |-val1
      |   |- ?
      |
      |-val2
      |   |- ?
      |
      |-val3
          |- ?

get the attribute this node represents (in this case, the root node):
    dt.attr --> attr1

get the branches of a node (in this case, the root node):
    dt.branches --> val1, val2, val3

get the node at the end of a branch:
    dt.branches[val1] --> another decision tree object

'''

class DecisionTree:
    def __init__(self):
        self.attr = '?' # value of current node; the attribute this node represents
        self.branches = {} # branches from this node; the values this attribute can take

    def add_node(self, node):
        if len(node)!=1: exit('Node must be a single dict item (key-value pair)')
        
        # get attribute (dict.key) and values of attribute (dict.value) from node (dict)
        unwrap = lambda dict: (list(node.keys())[0], list(node.values())[0])
        
        attribute, values = unwrap(node)

        self.attr = attribute
        self.branches = {v:DecisionTree() for v in values} # assign a new attribute node to the end of each value branch

    def __str__(self, level=0):
        line = lambda level,string: ''.join(['    |    ' if i%2==0 else '         ' for i in range(level-1)]) + ('    |----' if level>0 else '') + string + '\n'

        s = line(level, self.attr)
        for branch in self.branches:
            s += line(level+1, branch)
            s += self.branches[branch].__str__(level+2)
        return s
