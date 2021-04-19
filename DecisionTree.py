class DecTree:

    def __init__(self, attr='?', values=[]):
        # attr: string stating the attribute this node represents
        if not isinstance(attr, str): raise TypeError("attribute must be a string")

        # values: list of strings representing the values branches can have
        if (not isinstance(values, list) # values must be a list
        or not all([isinstance(v,str) for v in values])): # all items in values must be strs
            raise TypeError("values must be a list of strings")

        # make sure attr is given if values are given
        if attr=='?' and values: raise ValueError("cannot assign values to attribute '?'")
        
        self.attr = attr
        self.values = {val:DecTree() for val in values} # new empty tree at end of each value branch

    def add_node(self, value, child_attr='?', child_values=[]):
        # function to assign new attribute node to end of value branch
        if value not in self.values: raise ValueError(f"'{value}' is not a value of '{self.attr}'")
        self.values[value] = DecTree(child_attr, child_values)

    def get_node(self, attr):
        # traverse tree and return node with given attr

        if self.attr==attr: return self

        for value in self.values:
            child = self.values[value]
            if child.get_node(attr): return child.get_node(attr)

        raise ValueError(f"'{attr}' not in tree")
    
    def __str__(self, level=0):
        lines = [] 
        indent = '\t'
        lines.append(indent*level + self.attr)
        for value in self.values:
            child = self.values[value]
            lines.append(indent*(level+1) + value)
            lines.append(child.__str__(level+2))

        return '\n'.join(lines)