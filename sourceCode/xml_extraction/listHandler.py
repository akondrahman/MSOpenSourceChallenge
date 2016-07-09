# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:07:19 2015

@author: USRAAKO
"""
import wordConverter, reader 

import os, sys
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))




def get_stop_words():
  lisToRet =  ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
  'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
  'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
  'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
  'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
  'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
  'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
  'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
  'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
  'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
  'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
  'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']    
  return lisToRet    

stopWordList =  get_stop_words()

cKeywordList = ["auto", "break", "case", "char", "const", "continue", 
                "default", "do", "double", "else", "enum", "extern",  
                "float", "for", "fprintf", "goto", "if", "int", "long", "printf", 
                "register", "return", "short", "signed", "sizeof", "static", "struct", 
                "switch", "typedef", "union", "unsigned", "void", "volatile", 
                "while"]

cppKeyWordFileName="CPP_KW.txt";
cppKeywordList = reader.readKeywordFile(cppKeyWordFileName) ; 
#print "CPP Keywords ", cppKeywordList ;

cSharpKeyWordFileName="CSHARP_KW.txt";
cSharpKeywordList = reader.readKeywordFile(cSharpKeyWordFileName) ; 
#print "CSharp Keywords ", cSharpKeywordList ;

JavaKeyWordFileName="JAVA_KW.txt";
JavaKeywordList = reader.readKeywordFile(JavaKeyWordFileName) ; 
#print "Java Keywords ", JavaKeywordList ;

def removeNumeralsFromList(listParam):
    tempList=[];
    finalList=[];
    for listO in listParam:
        fileNameForList = listO[0];
        #print "Filename ", fileNameForList ;
        #print "List before numeral handling: ", listO ;     
        tempList.append(fileNameForList);
        iter_listO = iter(listO);
        next(iter_listO);
        for tokenStr in iter_listO:
            modifiedTokenStr =  wordConverter.removeNumeralsFromWord(tokenStr);
            tempList.append(modifiedTokenStr);
        finalList.append(tempList);
        #print "List after numeral handling: ", tempList ;
        tempList = [] ; 
    return finalList ;    
    
def removeSpecialCharsFromList(listParam):
    tempList=[];
    finalList=[];
    for listO in listParam:
        fileNameForList = listO[0];
        #print "Filename ", fileNameForList ;
        #print "List before special character handling: ", listO ;     
        tempList.append(fileNameForList);    
        
        iter_listO = iter(listO);
        next(iter_listO);
        for tokenStr in iter_listO:
            modifiedTokenStr =  wordConverter.removeSpecialCharsFromWord(tokenStr);  
            tempList.append(modifiedTokenStr);
        finalList.append(tempList);
        #print "List after special character handling: ", tempList ;
        tempList = [] ; 
    return finalList ;   

def removeDelimitersFromList(listParam):
    tempList=[];
    finalList=[];
    for listO in listParam:
        fileNameForList = listO[0];
        #print "Filename ", fileNameForList ;
        #print "List before special character handling: ", listO ;     
        tempList.append(fileNameForList);    
        
        iter_listO = iter(listO);
        next(iter_listO);
        for tokenStr in iter_listO:
            modifiedTokenStr =  wordConverter.removeDelimitersFromWord(tokenStr);  
            tempList.append(modifiedTokenStr);
        finalList.append(tempList);
        #print "List after special character handling: ", tempList ;
        tempList = [] ; 
    return finalList ;   


def splitUnderscores(listParam):
    tempList=[];
    finalList=[];
    underscoreStr="_";
    splittedTokenList = [] ;
    for listO in listParam:
        #print "List before underscore handling: ", listO ;     
        for tokenStr in listO:
            if tokenStr is not None  and underscoreStr in tokenStr:            
                splittedTokenList = wordConverter.splitUnderscores(tokenStr);  
                tempList.extend(splittedTokenList);           
            else:
                tempList.append(tokenStr);
        finalList.append(tempList);
        #print "List after underscore handling: ", tempList ;
        tempList = [] ; 
    return finalList ;   


def splitSpaces(listParam):
    tempList=[];
    finalList=[];
    spaceStr=" ";
    splittedTokenList = [] ;
    for listO in listParam:
        #print "List before space handling : ", listO ;     
        for tokenStr in listO:
            if tokenStr is not None  and spaceStr in tokenStr:            
                splittedTokenList = wordConverter.splitSpaces(tokenStr);  
                tempList.extend(splittedTokenList);           
            else:
                tempList.append(tokenStr);
        finalList.append(tempList);
        #print "List after space handling: ", tempList ;
        tempList = [] ; 
    return finalList ;   

    
def handleCamelNPascalCaseInList(listParam):
    tempList=[];
    finalList=[];
    for listO in listParam:
        fileNameForList = listO[0];
        #print "Filename ", fileNameForList ;
        #print "List before camel case handling: ", listO ;     
        tempList.append(fileNameForList);    
        
        iter_listO = iter(listO);
        next(iter_listO);
        for tokenStr in iter_listO:
            modifiedTokenStr = wordConverter.splitCamelNPascalCase(tokenStr);  
            tempList.append(modifiedTokenStr);
        finalList.append(tempList);
        #print "List after camel case handling: ", tempList ;
        tempList = [] ; 
    return finalList ;      
    
def removeSmallLenghtedTokens(listParam):
    #this method removes tokens that are less than three in length from the list 
    tempList=[];
    finalList=[];
    for listO in listParam:
        fileNameForList = listO[0];
        #print "Filename ", fileNameForList ;
        #print "List before removing small lenghted tokens : ", listO ;     
        tempList.append(fileNameForList);            
        iter_listO = iter(listO);
        next(iter_listO);
        for tokenStr in iter_listO:
            if type(tokenStr) is str:
               if len(tokenStr) > 2: 
                  tempList.append(tokenStr);
        finalList.append(tempList);
        #print "List after removing small lenghted tokens: ", tempList ;
        tempList = [] ; 
    return finalList ;

def removeStopWords(listParam):
    #this method removes tokens that are basically stop words from the list 
    tempList=[];
    finalList=[];
    for listO in listParam:
        fileNameForList = listO[0];
        #print "Filename ", fileNameForList ;
        #print "List before removing stop words : ", listO ;     
        tempList.append(fileNameForList);            
        iter_listO = iter(listO);
        next(iter_listO);
        for tokenStr in iter_listO:
            if tokenStr not in stopWordList:
                tempList.append(tokenStr);
        finalList.append(tempList);
        #print "List after removing stop words : ", tempList ;
        tempList = [] ; 
    return finalList ; 

def removeAllLanguageKeywords(listParam):
    list_C_output = removeCKeywords(listParam);
    list_CPP_output = removeCPPKeywords(list_C_output); 
    list_CSharp_output = removeCSharpKeywords(list_CPP_output);
    list_Java_output = removeJavaKeywords(list_CSharp_output);
    return list_Java_output  ;  


def removeJavaKeywords(listParam):
    #this method removes tokens that are Java keywords, from the list 
    tempList=[];
    finalList=[];
    for listO in listParam:
        fileNameForList = listO[0];
        #print "Filename ", fileNameForList ;
        #print "List before removing Java keywords: ", listO ;     
        tempList.append(fileNameForList);            
        iter_listO = iter(listO);
        next(iter_listO);
        for tokenStr in iter_listO:
            if tokenStr not in JavaKeywordList :
                tempList.append(tokenStr);
        finalList.append(tempList);
        #print "List after removing Java keywords: ", tempList ;
        tempList = [] ; 
    return finalList ;          

def removeCSharpKeywords(listParam):
    #this method removes tokens that are C# keywords, from the list 
    tempList=[];
    finalList=[];
    for listO in listParam:
        fileNameForList = listO[0];
        #print "Filename ", fileNameForList ;
        #print "List before removing C# key words : ", listO ;     
        tempList.append(fileNameForList);            
        iter_listO = iter(listO);
        next(iter_listO);
        for tokenStr in iter_listO:
            if tokenStr not in cSharpKeywordList:
                tempList.append(tokenStr);
        finalList.append(tempList);
        #print "List after removing C# key words : ", tempList ;
        tempList = [] ; 
    return finalList ;          


def removeCPPKeywords(listParam):
    #this method removes tokens that are CPP keywords, from the list 
    tempList=[];
    finalList=[];
    for listO in listParam:
        fileNameForList = listO[0];
        #print "Filename ", fileNameForList ;
        #print "List before removing CPP key words : ", listO ;     
        tempList.append(fileNameForList);            
        iter_listO = iter(listO);
        next(iter_listO);
        for tokenStr in iter_listO:
            if tokenStr not in cppKeywordList:
                tempList.append(tokenStr);
        finalList.append(tempList);
        #print "List after removing CPP key words : ", tempList ;
        tempList = [] ; 
    return finalList ;          

def removeCKeywords(listParam):
    #this method removes tokens that are C keywords, from the list 
    tempList=[];
    finalList=[];
    for listO in listParam:
        fileNameForList = listO[0];
        #print "Filename ", fileNameForList ;
        #print "List before removing C key words : ", listO ;     
        tempList.append(fileNameForList);            
        iter_listO = iter(listO);
        next(iter_listO);
        for tokenStr in iter_listO:
            if tokenStr not in cKeywordList:
                tempList.append(tokenStr);
        finalList.append(tempList);
        #print "List after removing C key words : ", tempList ;
        tempList = [] ; 
    return finalList ;       


def format_using_stemmer(listParam): 
  #print len(listParam)  
  output_list = []
  formatted_list = []
  from nltk.stem.porter import PorterStemmer
  stemmer_obj = PorterStemmer() 
  for subList in listParam:
    formatted_list = [stemmer_obj.stem(token) for token in subList]
    output_list.append(formatted_list)
    formatted_list = []
  return output_list
      