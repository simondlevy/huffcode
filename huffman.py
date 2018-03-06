'''
Huffman Code implementation and example

Copyright (C) 2018 Simon D. Levy

This file is part of huffcode.
 
Huffcode is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Huffcode is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with huffcode.  If not, see <http://www.gnu.org/licenses/>.
'''

from numpy import sum
from bintree import LeafNode, InternalNode

def remove_lowest(q):
    '''
    Removes lowest-valued node in a priority queue.
    Returns the node and the modified queue.
    '''
    fmin = 1.0
    pos = -1
    
    for n,k in zip(q, range(len(q))):
        if n.value < fmin:
            fmin = n.value
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
            code += [0]
            t = t.left
        else:
            code += [1]
            t = t.right
        
    return code


if __name__ == '__main__':

    import urllib.request

    # Call me Ishmael
    URL = 'http://home.wlu.edu/~levys/csci121w2018/data/mobydick.txt'

    # Read in the entire text at once, converting it to lower-case
    text = str(urllib.request.urlopen(URL).read().lower())

    # Build dictionary of letter occurrence counts
    d = {}
    for c in 'abcdefghijklmnopqrstuvwxz':
        d[c] = text.count(c)

    # Convert the counts into a dictionary {label:frequency}
    total = sum([d[c] for c in d.keys()])
    d = {c: d[c]/total for c in d.keys()}

    # Convert the dictionary into a Huffman-code tree
    t = hufftree(d)

    # Look up the letters in the tree
    for c in d.keys():
        print(c, huffcode(c, t))


    
