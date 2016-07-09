# -*- coding: utf-8 -*-
"""
Created on Thu Jul 02 13:35:41 2015

@author: USRAAKO
"""

def getFileLevelAllFiles_TokenExtractor(fileNameParam):
    import tokenExtractor as TE


    listToret = [] ;
    listToret = TE.giveFileLevelTokens(fileNameParam)
    #print "THE LISSST: ", listToret ;
    return listToret;
    
    
    
def getNameSpaceLevelAllFiles_TokenExtractor(dirParam, extensionParam):
    import tokenExtractor as TE
    import os, sys
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))    
    listToret = [] ;
    for fileObj in os.listdir(dirParam):
        if fileObj.endswith(extensionParam):
            listToret = TE.giveNameSpaceLevelTokens(dirParam + fileObj);
    #print "THE LISSST: ", listToret ;
    return listToret;    