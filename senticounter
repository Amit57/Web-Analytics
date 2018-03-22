#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:53:14 2018

@author: amit
"""
def run(file):
    posDict={}
    
    positivewords = set()
    wordsFile = open('positive-words.txt')
    for word in wordsFile:
        positivewords.add(word.strip())
    wordsFile.close()
    
    reviewFile = open(file)
    for review in reviewFile:
        review = review.lower().strip()
        words = review.split(' ')
        words = list(set(words))
        for word2 in words:
            if word2 in positivewords:
                if word2 in posDict:
                    posDict[word2] += 1
                else:
                    posDict[word2] = 1
    reviewFile.close()
    return(posDict)
    

if __name__ == "__main__": 
    print(run('textfile'))      
