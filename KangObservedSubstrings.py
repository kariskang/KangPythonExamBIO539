#!/usr/bin/env python3



'''
    Count observed substrings of size k for sequence data stored as an unbroken string in a text file
    
    Args: 
        1: a txt file with sequence data, no lines
        2: a substring length
    
    Return: 
        List of substring sequences of length k and how many times they occur in the sequence
        The total number of unique observed substrings 
        
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

for seq, count in substring.items(): #for the key and count in the dict substring, print "key, count"
    print(seq, count)
    
print("The total number of unique observed substrings of length " + str(k) + " is " + str(len(substring))) 