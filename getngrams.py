#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:38:41 2018

@author: amit
"""


"""

The script includes the following pre-processing steps for text:
- Sentence Splitting
- Term Tokenization
- Ngrams
- POS tagging

The run function includes all 2grams of the form: <ADVERB> <ADJECTIVE>

POS tags list: https://www.l ing.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
"""


import nltk
from nltk.util import ngrams
import re
from nltk.tokenize import sent_tokenize
from nltk import load



def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex



def processSentence(sentence,posLex,negLex,tagger):
    result=[]
     
    #tokenize the sentence
    terms = nltk.word_tokenize(sentence.lower())
    POStags=['NN'] # POS tags of interest 		
    POSterms=getPOSterms(terms,POStags,tagger)
    nouns=POSterms['NN']
    ngram = ngrams(terms,4) #compute 4-grams 
        #get the results for this sentence 
   	 #for each 2gram
    for ng in ngram:  
        if ng[0] == 'not' and (ng[2] in posLex or ng[2] in negLex) and ng[3] in nouns: 
            result.append(ng)

    return result


# return all the terms that belong to a specific POS type
def getPOSterms(terms,POStags,tagger):
	
    tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence

    POSterms={}
    for tag in POStags:POSterms[tag]=set()

    #for each tagged term
    for pair in tagged_terms:
        for tag in POStags: # for each POS tag 
            if pair[1].startswith(tag): POSterms[tag].add(pair[0])

    return POSterms


def run(fpath):

    #make a new tagger
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)
    posLex=loadLexicon('positive-words.txt')
    negLex=loadLexicon('negative-words.txt')

    #read the input
    f=open(fpath)
    text=f.read().strip()
    f.close()

    #split sentences
    sentences=sent_tokenize(text)
    #print ('NUMBER OF SENTENCES: ',len(sentences))

    reqdString=[]

    # for each sentence
    for sentence in sentences:

        sentence=re.sub('[^a-zA-Z\d]',' ',sentence)#replace chars that are not letters or numbers with a spac
        sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces

        
        reqdString+=processSentence(sentence,posLex,negLex,tagger)
		
    return reqdString




def getTop3(D):
    newD = sorted(D, key=D.get, reverse=True)[:3]
    return newD


if __name__=='__main__':
    D = {'a':10, 'b':843, 'c': 39, 'd':300, 'John':1111, 'Ted': 3333, 'New York':7,'California':6,'North Carolina':250}
    print (getTop3(D))
    print (run('input.txt'))

 


 