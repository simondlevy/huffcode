import numpy as np
from pprint import pprint
import operator

class Node(object):

    def __init__(self, label, freq):
        
        self.label = label
        
        self.freq = freq

class LeafNode(Node):

    def __init__(self, label, freq):
        
        Node.__init__(self, label, freq)

    def __str__(self):

        return self.label  + ':' + str(self.freq)

class InternalNode(Node):
    
    def __init__(self, left, right):
        
        Node.__init__(self, left.label+right.label, left.freq+right.freq)
        

def huffcode(freqdic):
    '''
    Builds and returns a Huffman-code dictionary from a dictionary of
    letter frequencies, by running the "Alternative Description" algorithm
    from Prof. Sprenkle's slide #38
    '''

    # Create a leaf node for each symbol, labeled by its frequency, and add to a queue
    # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    q = [LeafNode(label, freq) for label, freq in sorted(freqdic.items(), key=operator.itemgetter(1))]

    # While there is more than one node in the queue
    while len(q) > 1:

        # Remove the two nodes of lowest frequency
        n1,n2 = q[0],q[1]
        q = q[2:]

        print(n1)
        
        # Create a new internal node with these two nodes
        # as children and with frequency equal to the sum
        # of the two nodes' probabilities

        break

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

    
