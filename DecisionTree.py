'''
attr1 == valueA1:
    attr2 == valueB1:
        attr3 == valueD3: Yes
    attr2 == valueB2:
attr1 == valueA2:
    attr2 == valueC1:
    attr2 == valueC2:
attr1 == valueA3:
'''

class Node:
    def __init__(self, attribute='?', values=[]):
        if attribute=='?' and values: raise ValueError(f"'?' is the defualt attribute and thus cannot be given values {values}")
        self.__attribute = attribute # attribute this node represents
        self.__children = {value: Node('?') for value in values}

    def set_node(self, attribute, values=[]):
        if attribute=='?': raise ValueError("'?' is only a default value and cannot be set as the attribute of a node")
        self.__attribute = attribute
        self.__children = {value: Node('?') for value in values}

    def get_A(self): 
        return self.__attribute

    def get_c(self): 
        return [value for value in self.__children]

    def get_child(self, value=None):
        if value==None: return self.__children # return all children as dict if no arg given
        else: return self.__children[value] # return child at value

    def set_child(self, value, node):
        if node.get_A()=='?': raise ValueError("'?' is only a default value and cannot be set as the attribute of a node")
        if value not in self.__children: raise ValueError(f"{self.__attribute} can have values {[value for value in self.__children]}, not '{value}'")
        self.__children[value] = node

    def __str__(self, level=0):

        indent = lambda level: '\t'*level

        s = ''

        if self.__children:
            # print all possible values
            for value, child in self.__children.items():
                s += '\n' + indent(level) + self.__attribute + ' == ' + value + ': '
                s += child.__str__(level+1)
        else: 
            return self.__attribute + '\n'

        return s