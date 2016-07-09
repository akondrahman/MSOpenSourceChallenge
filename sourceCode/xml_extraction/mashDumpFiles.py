# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 16:24:50 2016

@author: akond
"""



def readDumpFile(fileNameParam): 
    import pickle
    listToRet=[]
    listToUse = pickle.load( open( fileNameParam, "rb" ) )
    for subList in listToUse:
        iter_list = iter(subList);
        next(iter_list);
        for tokens in iter_list: 
            listToRet.append(tokens)
    #print "tokens: ", listToRet
    print "--------------Completed Loading Tokens---------------"        
    return listToRet          
    
import os, dumpModule 
dirToMash="/Users/akond/Documents/Simila_Work/xml_extraction_output/chrome/"
outputDir="/Users/akond/Documents/Simila_Work/xml_extraction_output/"
fileName_Output="Complete_Chrome" + ".dump"
extensionParam="dump"
completeList = []
for fileObj in os.listdir(dirToMash):
    if fileObj.endswith(extensionParam):
       fileName= dirToMash +   fileObj 
       print "-----------------------------"
       completeList.append(readDumpFile(fileName))
#print "The complete list ... ",completeList       
dumpModule.dumpListToFile(dirToMash+fileName_Output, completeList) 