#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 19:17:44 2018

@author: amit
"""

from bs4 import BeautifulSoup
import re
import time
import requests

def getCritic(review):
    
    critic='NA' 
    criticChunk=review.find('a',{'href':re.compile('/critic/')})
    if criticChunk: critic=criticChunk.text
    
    return(critic)

def getRating(review):
    
    rating='NA' 
    ratingChunk=review.find('div',{'class':re.compile('fresh')})
    if ratingChunk: 
        rating ='fresh'
    elif review.find('div',{'class':re.compile('rotten')}):
        rating = 'rotten'
        
    return(rating)
    
def getSource(review):
    
    source='NA' 
    sourceChunk=review.find('em',{'class':re.compile('subtle')})
    if sourceChunk: source=sourceChunk.text
    
    return(source)

def getDate(review): 
    
    date='NA' 
    dateChunk=review.find('div',{'class':re.compile('review_date')})
    if dateChunk: date=dateChunk.text
    
    return(date)
    
def getTextLen(review):
    
    length='NA'
    lengthChunk=review.find('div',{'class':'the_review'})
    if lengthChunk: length=lengthChunk.text.strip()
    
    return(str(len(length)))
    	
    
    

    



    

