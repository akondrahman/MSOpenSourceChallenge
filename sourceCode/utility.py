# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 16:20:03 2016

@author: akond
"""



import numpy as np 
def getScores(fileNameParam, origFileNameParam):    
  negativeScores = []
  positiveScores=[]
  allScores=[]  
  fileToread = open(fileNameParam, 'r')    

  for score_line in fileToread:
    score = float(score_line)
    if score >= 0.0: 
      positiveScores.append(score) 
    elif score < 0.0: 
      negativeScores.append(score)
    allScores.append(score)
  print "#####"  
  print "File name: {}, total count: {}, pos: {}, neg: {} ".format(origFileNameParam, len(allScores), len(positiveScores), len(negativeScores))      
  print "All: mean={}, median={} ".format(np.mean(allScores), np.median(allScores))        
#  print "Pos: mean={}, median={} ".format(np.mean(positiveScores), np.median(positiveScores))          
#  print "Neg: mean={}, median={} ".format(np.mean(negativeScores), np.median(negativeScores))   
  print "#####"             