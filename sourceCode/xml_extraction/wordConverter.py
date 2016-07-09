# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 09:41:23 2015

@author: USRAAKO
"""
import re, string
 
def removeDelimitersFromWord(wordParam):
    if wordParam is not None: 
        exclude = ['\n', '\t'] ;
        strOutput = ''.join(ch for ch in wordParam if ch not in exclude);    
        return strOutput ;



def removeSpecialCharsFromWord(wordParam):
    if wordParam is not None: 
        exclude = set(string.punctuation) ;
        strOutput = ''.join(ch for ch in wordParam if ch not in exclude);    
        return strOutput ;    
    
def removeNumeralsFromWord(wordParam):
    if wordParam is not None:
        strOutput = ''.join([letter for letter in wordParam if not letter.isdigit()]);
        return strOutput ;    
    
    
def splitCamelNPascalCase(strParam):
    if type(strParam) is str:
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', strParam);
        return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1).lower();   
    
def splitUnderscores(strParam):
        underscoreStr="_";
        tempList = [] ;        
        if strParam is not None:
            tempList = strParam.split(underscoreStr);
        return tempList ;    
    
def splitSpaces(strParam):
        spaceStr=" ";
        tempList = [] ;        
        if strParam is not None:
            tempList = strParam.split(spaceStr);
        return tempList ;   