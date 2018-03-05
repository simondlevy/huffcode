import numpy as np
from pprint import pprint

def huffcode(freqdic):
    '''
    Builds and returns a Huffman-code dictionary from a dictionary of
    letter frequencies
    '''

    pprint(freqdic)

    huffd = {}

    return huffd

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
    print(hufftext('mobydick.txt'))

    
