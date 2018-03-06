'''
Support for simple binary trees

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


