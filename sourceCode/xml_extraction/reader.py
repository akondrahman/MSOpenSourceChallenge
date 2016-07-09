# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:04:11 2015

@author: USRAAKO
"""

def readKeywordFile(fileName):
    import os, sys
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))    
    listToRet = [] ;
    fileO = open(fileName, 'r');
    for line in fileO:
        line = line.strip('\n');
        line = line.strip('\t');
        listToRet.append(line);
    return listToRet ;    