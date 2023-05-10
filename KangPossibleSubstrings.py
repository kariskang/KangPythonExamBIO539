#!/usr/bin/env python3



'''
   
    Count possible substrings of size k for sequence data stored as an unbroken string in a text file
    
    Args: 
        1: a txt file with sequence data, no lines
        2: a substring length
    
    Return: 
        The number of possible substrings of length k for a given sequence
        
        
'''

import sys

k = int(sys.argv[2]) #the length of the substring the user wants to process their data with 
f = open(sys.argv[1], 'r') 
seqfile = f.read()

substring = {} #empty dict to store substring sequences of length k and their counts

for i in range(0,len(seqfile) - (k-1)): #i = any starting point in the original sequence from which a full subsequence can be completed
    subseq = seqfile[i:i+k] #any k long subsequence that can be found in original sequence
    if subseq in substring: 
        substring[subseq] += 1 #if the subsequence is already in the dict substring then add a count
    else: 
        substring[subseq] = 1 #if the subsequence isn't in the dict substring then add it

print("The number of possible substrings of length " + str(k) + " is " + str(sum(substring.values())))