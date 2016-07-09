# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:11:38 2015

@author: USRAAKO
"""

def dumpListToFile(fileParam, listParam):
    import pickle 
    with open(fileParam, 'wb') as f:
        pickle.dump(listParam, f);