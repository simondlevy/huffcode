import numpy as np
from pprint import pprint
import operator

# Some classes supporting Huffman-code binary trees

class Node(object):

    def __init__(self, label, freq):
        
        self.label = label
        self.freq = freq

    def __str__(self):

        return self.label  + ':' + str(self.freq)
    
class LeafNode(Node):

    def __init__(self, label, freq):
        
        Node.__init__(self, label, freq)
        self.isleaf = True

class InternalNode(Node):
    
    def __init__(self, left, right):
        
        Node.__init__(self, left.label+right.label, left.freq+right.freq)
        self.left = left
        self.right = right
        self.isleaf = False

    def __str__(self):

        return Node.__str__(self) + " = " + self.left.label + ", " + self.right.label

    def isleaf(self):

        return False


# Support for priority queue
# XXX No muy pythonista!
def remove_lowest(q):

    fmin = 1.0
    pos = -1
    
    for n,k in zip(q, range(len(q))):
        if n.freq < fmin:
            fmin = n.freq
            pos = k
        
    return q[pos], q[:pos] + q[pos+1:]

    

def hufftree(freqdic):
    '''
    Builds and returns a Huffman-code tree from a dictionary of
    letter frequencies, by running the "Alternative Description" algorithm
    from Prof. Sprenkle's slide #38
    '''

    # 1. Create a leaf node for each symbol, labeled by its frequency, and add to a queue
    q = [LeafNode(label, freqdic[label]) for label in freqdic.keys()]

    # 2. While there is more than one node in the queue
    while len(q) > 1:

        # a) Remove the two nodes of lowest frequency
        node1,q = remove_lowest(q)
        node2,q = remove_lowest(q) 
        
        # b) Create a new internal node with these two nodes
        #    as children and with frequency equal to the sum
        #    of the two nodes' probabilities
        node = InternalNode(node1, node2)

        # c) Add the new node to the queue
        q.append(node)

    # 3. The remaining node is the tree's root node
    return q[0]

def huffcode(c, t):
    '''
    Looks up the character C in the Huffman-code tree T
    '''

    code = []

    while (not t.isleaf):

        if c in t.left.label:
            code = code + [0]
            t = t.left
        else:
            code = code + [1]
            t = t.right
        
    return code



def hufftext(filename):
    '''
    Builds and returns a Huffman-code dictionary built from letters in
    named text file
    '''

    # Read in the entire text at once, converting it to lower-case
    text = open(filename).read().lower()

    # Build dictionary of letter occurrence counts
    d = {}
    for c in 'abcdefghijklmnopqrstuvwxz':
        d[c] = text.count(c)

    # Convert the counts into a dictionary {label:frequency}
    total = np.sum([d[c] for c in d.keys()])
    d = {c: d[c]/total for c in d.keys()}

    # Convert the dictionary into a Huffman-code tree
    t = hufftree(d)

    # Make a new dictionary from the Huffman-code tree
    return {c:huffcode(c,t) for c in d.keys()}

if __name__ == '__main__':

    d = {'a':.32, 'b':.25, 'c':.20, 'd':.18, 'e':.05}

    t = hufftree(d)

    for c in d.keys():
        print(c, huffcode(c, t))

    # Call me Ishmael
    #pprint(hufftext('mobydick.txt'))

    
