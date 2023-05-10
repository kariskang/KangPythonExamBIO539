#!/usr/bin/env python3
'''
    Calculate linguistic complexity of sequence data imported as a text file 
    Args: 
        1: a txt file with sequence data, no lines
    
    Return: 
        Linguistic complexity of sequence data
        The total number of unique observed substrings and unique possible substrings
        
'''
import sys

f = open(sys.argv[1], 'r') 
seqfile = f.read()

substring = {} #dict for all observed substring sequences for every substring length, and how many times those sequences occur

for start in range(0,len(seqfile)+1): 
#start = any starting point in the original sequence; add 1 to string length in range so the last character doesn't get cut off
    for end in range(start+1,len(seqfile)+1): #end = any end point in original sequence
        #added +1 to start of range bc it kept counting blank spaces as subsequences otherwise?
        #added +1 to end of range so last character doesn't get cut off
        subseq = seqfile[start:end] #any subsequence that can be found between starting or ending point in original sequence
        if subseq in substring: 
            substring[subseq] += 1 #if the subsequence is already in the dict substring then add a count
        else: 
            substring[subseq] = 1 #if the subsequence isn't in the dict substring then add it

obs_sum = len(substring) #count of all unique substrings in dict aka number of unique substrings observed
pos_sum = sum(substring.values()) #sum of all substring occurences in dict aka number of unique substrings possible
lcomp = obs_sum/pos_sum # linguistic complexity calculation


print("The linguistic complexity of this sequence is " + str(lcomp))
print("The total number of unique observed substrings is " + str(obs_sum) + " and number of unique possible substrings is " + str(pos_sum))

