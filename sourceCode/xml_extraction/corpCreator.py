# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:41:15 2015

@author: USRAAKO
"""

import  listHandler, dumpModule  

def generateCorpus(rawTokenList, fileparamToDump):
    
    ###Order of execution is extremely important 
    ## 1
    outputList_NumeralsRemoved = listHandler.removeNumeralsFromList(rawTokenList)
    ## 2
    outputList_UnderscoreHandled = listHandler.splitUnderscores(outputList_NumeralsRemoved)
    ## 3
    outputList_CamelNPascalHandled = listHandler.handleCamelNPascalCaseInList(outputList_UnderscoreHandled)
    ## 4
    outputList_SplitSpaces = listHandler.splitSpaces(outputList_CamelNPascalHandled)
    ## 5 
    outputList_SpecialCharsRemoved = listHandler.removeSpecialCharsFromList(outputList_SplitSpaces)
    ## 6 
    outputList_SmallTokensRemoved = listHandler.removeSmallLenghtedTokens(outputList_SpecialCharsRemoved)
    ## 7 
    outputList_StopWordGone = listHandler.removeStopWords(outputList_SmallTokensRemoved)
    ## 8 
    outputList_AllKeyWordsRemoved = listHandler.removeAllLanguageKeywords(outputList_StopWordGone)
    ##9 
    output_DelimiterRemoved = listHandler.removeDelimitersFromList(outputList_AllKeyWordsRemoved)
    ##10
    output_porter_stemmed = listHandler.format_using_stemmer(output_DelimiterRemoved)    
    print "--------------------------- ALMOST THERE! ----------------------------"
    print "I am done [:-)], current length of the list: ", len(output_porter_stemmed)     
    ## Finally 
    dumpModule.dumpListToFile(fileparamToDump, output_porter_stemmed)    
    
    return "Succesfully generated corpus of project! Length of corpus"+str(len(output_porter_stemmed)) 