# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 16:35:16 2016

@author: akond
"""



import utility , os 
dirParam="/Users/akond/Documents/Personal/gitMisc/MS-OpenSourceChallenge/Sent2VecOutput/small_model_100000_scores_only/"
fileCnt=0
for fileObj in os.listdir(dirParam):
  if fileObj.endswith("txt"):
    fileCnt = fileCnt + 1
    fileName= dirParam +   fileObj       
    utility.getScores(fileName,fileObj)