import numpy as np
import math as m
from numpy.core.defchararray import array

'''this function take a list/array of numbers as function 
    and return a list of numbers after perform 1+log(input)'''
def caluc_termFrequncy_weight(termFrequncy):
    if termFrequncy==0:
        return 0
    else:
        return list(1+(np.log(termFrequncy)/m.log(10)))

'''it takes number of documents in the folder and returns the idf'''
def caluc_idf(numberOfDocx,documentFrequncy):
    return m.log(numberOfDocx/documentFrequncy)

''' it will be used for each term'''
def caluc_termTFidf(termFrequncy_weight,idf):
    return termFrequncy_weight*idf

def document_Length(TFidfsOfDocument):
    return np.linalg.norm(array(TFidfsOfDocument))

'''this function take TFidf of a term in a spacific document 
    and the length of that spacific document and returns the normlize_TFidf'''
def normlize_TFidf(termTFidf,documentLength):
    return termTFidf/documentLength

'''this fucntion takes a list of the normlize TFidf of all terms 
    in a spacific document and a list the normlize TFidf of all terms 
    in the query and return "the score for that spacific document"=(similiraty
    between that document and the query)'''
def caluc_similiraty(normlize_TFidfsOfDocument,normlize_TFidfsOfQuery):
    return (np.dot(normlize_TFidfsOfDocument,normlize_TFidfsOfQuery))




