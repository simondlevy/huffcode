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

class InternalNode(Node):
    
    def __init__(self, left, right):
        
        Node.__init__(self, left.label+right.label, left.freq+right.freq)
        self.left = left
        self.right = right

    def __str__(self):

        return Node.__str__(self) + " = " + self.left.label + ", " + self.right.label


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

    

def huffcode(freqdic):
    '''
    Builds and returns a Huffman-code dictionary from a dictionary of
    letter frequencies, by running the "Alternative Description" algorithm
    from Prof. Sprenkle's slide #38
    '''

    # 1. Create a leaf node for each symbol, labeled by its frequency, and add to a queue
    q = [LeafNode(label, freqdic[label]) for label in freqdic.keys()]

    # 2. While there is more than one node in the queue
    while len(q) > 1:

        for n in q:
            print(n)
        print('')

        # a) Remove the two nodes of lowest frequency
        node1,q = remove_lowest(q)
        node2,q = remove_lowest(q) 
        
        # b) Create a new internal node with these two nodes
        #    as children and with frequency equal to the sum
        #    of the two nodes' probabilities
        node = InternalNode(node1, node2)

        # c) Add the new node to the queue
        q.append(node)


    return {}

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

    # Convert the counts into frequencies
    total = np.sum([d[c] for c in d.keys()])
    d = {c: d[c]/total for c in d.keys()}

    # Return Huffman-code dictionary built from letter-frequency dictionary
    return huffcode(d)

if __name__ == '__main__':

    # Call me Ishmael
    pprint(hufftext('mobydick.txt'))

    
