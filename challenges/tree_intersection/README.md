# Intersection of binary trees
Finds the common values inside two binary trees.

## Challenge
Use a traversal method to iterate through both trees and find some way of distinguishing between two trees values.
Either using a set or a hash map would be valid ways.

## Solution
Traverse the first binary tree and add the values inside a set. The set does
the work of having to filter the array into only unique values. Now you should
traverse the second tree and check if that value of the current node is inside
that first set and if so add it the a results array and return it after looping
the second tree.
