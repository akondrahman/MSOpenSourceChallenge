# -*- coding: utf-8 -*-
"""
Created on Thu Jul 02 13:27:31 2015

@author: USRAAKO
"""
##To use Spark with Python uncomment the following line
#from pyspark import SparkContext
##

import resultGen, corpCreator
import datetime
import time
import os, sys
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

timestamp_ = time.time()
formatted_time = datetime.datetime.fromtimestamp(timestamp_).strftime('%Y-%m-%d %H:%M:%S')
print "Started at ", formatted_time

extensionParam="xml";

file_name="media"


dirParam_FileL="/Users/akond/Documents/Simila_Work/paikhana/swum-output-with-comments/chrome/" + file_name + "/"
outputDir="/Users/akond/Documents/Simila_Work/paikhana/token_filtered/"
toSave_FileLevel= file_name + ".dump"

#toSave_NamespaceLevel="Output_NamespaceL_Proj.dump"
#dirParam_NSpaceL="input_/nSpace_/"

##To use Spark with Python uncomment the following line
#sc=SparkContext(appName="Spark:XMLProcessing")
##
for fileObj in os.listdir(dirParam_FileL):
    if fileObj.endswith(extensionParam):
       fileName= dirParam_FileL +   fileObj
       print "-----------------------------"
       print "Starting token extraction for file name {}".format(fileName) 
       fileLevelRawTokens      =  resultGen.getFileLevelAllFiles_TokenExtractor(fileName)
       print "Original raw token count: ", len(fileLevelRawTokens)
       print "------------CREATING DUMP FILES ------------"
       toSave_FileLevel = outputDir + file_name + ".dump"
       print corpCreator.generateCorpus(fileLevelRawTokens, toSave_FileLevel) + " , at file level"
       #namespaceLevelRawTokens =  resultGen.getNameSpaceLevelAllFiles_TokenExtractor(dirParam_NSpaceL, extensionParam);



#print "------------";
#print corpCreator.generateCorpus(namespaceLevelRawTokens, toSave_NamespaceLevel) + " , at namespace level" ;



timestamp_ = time.time()
formatted_time = datetime.datetime.fromtimestamp(timestamp_).strftime('%Y-%m-%d %H:%M:%S')
print "Ended at ", formatted_time

