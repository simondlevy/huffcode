import numpy as np

def huffcode(freqdic):

    '''
    Builds and returns a Huffman-code dictionary from a dictionary of
    letter frequencies
    '''

    d = {}

    return d

def hufftext(filename):
    '''
    Builds and returns a Huffman-code dictionary built from letters in
    named text file
    '''

    # Read in the entire text at once, converting it to lower-case
    text = open(filename).read().lower()

    # Compute frequencies for the alphabetic characters
    for c in 'abcdefghijklmnopqrstuvwxz':
        print(c)

    # Build letter-frequency dictionary
    freqdic = {}

    # Return Huffman-code dictionary built from letter-frequency dictionary
    return huffcode(freqdic)

if __name__ == '__main__':

    print(hufftext('mobydick.txt'))

    
