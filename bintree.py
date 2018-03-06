'''
Support for simple binary trees
Simon D. Levy
CSCI 211
05 March 2018
'''

class _Node(object):

    def __init__(self, label, value):
        
        self.label = label
        self.value = value

    def __str__(self):

        return self.label  + ':' + str(self.value)
    
class LeafNode(_Node):

    def __init__(self, label, value):
        
        _Node.__init__(self, label, value)
        self.isleaf = True

class InternalNode(_Node):
    
    def __init__(self, left, right):
        
        _Node.__init__(self, left.label+right.label, left.value+right.value)
        self.left = left
        self.right = right
        self.isleaf = False

    def __str__(self):

        return _Node.__str__(self) + " = " + self.left.label + ", " + self.right.label


