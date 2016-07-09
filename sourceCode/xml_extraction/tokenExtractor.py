# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:00:07 2015

@author: USRAAKO
"""

def giveFileLevelTokens(xmlFileParam):
    import xml.etree.ElementTree as  ETLib
    import os, sys
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
    tree = ETLib.parse(xmlFileParam);
    theRoot = tree.getroot()
    tokenList = [] ;
    #fileList = [] ;
    listToRet = [] ;   
    fileCnt=0 
    for child in theRoot:
        tagParam = child.tag ;
        #if tagParam=="fileName": 
        if tagParam=="file":             
            # the first element of each list is the corresponding file name                    
            fileCnt += 1             
            fileNameStr = child.text.strip('\n');            
            tokenList.append(fileNameStr);
            for fileNameChild in child:
                fileNameChildTag = fileNameChild.tag;
                if fileNameChildTag=="token":
                    tokenList.append(fileNameChild.text);
            listToRet.append(tokenList);
            #print "Read all tokens of file #", fileCnt
            tokenList = [] ;
    ##appending all the token lists into one list aka vector 
    #listToRet.append(fileList);
    return listToRet ;               





def giveNameSpaceLevelTokens(xmlFileParam):
    import xml.etree.ElementTree as  ETLib
    import os, sys
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))    
    tree = ETLib.parse(xmlFileParam);
    theRoot = tree.getroot()
    tokenList = [] ;
    #fileList = [] ;
    listToRet = [] ;     
    for child in theRoot:
        tagParam = child.tag ;
        if tagParam=="nSpace": 
            # the first element of each list is the corresponding file name                    
            fileNameStr = child.text.strip('\n');            
            tokenList.append(fileNameStr);
            for fileNameChild in child:
                fileNameChildTag = fileNameChild.tag;
                if fileNameChildTag=="token":
                    tokenList.append(fileNameChild.text);
            listToRet.append(tokenList);
            tokenList = [] ;
    ##appending all the token lists into one list aka vector 
    #listToRet.append(fileList);
    return listToRet ;               
