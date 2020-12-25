import numpy as np
import math as m
from numpy.core.defchararray import array

'''this function take a list/array of numbers as function 
    and return a list of numbers after perform 1+log(input)'''



def calc_term_frequency_weight(term_frequency):
    if term_frequency == 0:
        return 0
    else:
        return (1+(np.log(term_frequency)/m.log(10)))


'''it takes number of documents in the folder and returns the idf'''

''' to get all number of docs we can implement a function that works on reading files function (toknization phase)'''
def calc_idf(number_of_docs, document_frequency):
    return m.log10(number_of_docs/document_frequency)


''' it will be used for each term'''


def calc_term_TFidf(term_frequency_weight, idf):
    return term_frequency_weight*idf


def document_length(TFidfs_of_document):
    return np.linalg.norm(array(TFidfs_of_document))


'''this function take TFidf of a term in a spacific document 
    and the length of that spacific document and returns the normlize_TFidf'''


def normalize_TFidf(term_TFidf, document_length):
    return term_TFidf/document_length


'''this fucntion takes a list of the normlize TFidf of all terms 
    in a spacific document and a list the normlize TFidf of all terms 
    in the query and return "the score for that spacific document"=(similiraty
    between that document and the query)'''

#doc normalized list = [0.67 , 0.511 , 0 , 0.53]
# query normalized list = [0 , 0 , 0.768 , 0.680]
#cos simi = 0.36
def calc_similarity(normalize_TFidfs_of_document, normalize_TFidfs_of_query):
    return (np.dot(normalize_TFidfs_of_document, normalize_TFidfs_of_query))


# vector_space_model = {
#   "docID": {"terms" :[{"term1" : [termfreq , tfw , idf , tfidf , normalize Tfidf]}
#                      {"term2" : [termfreq , tfw , idf , tfidf , normalize Tfidf]}] 
#             "docLength" : doclengthvalue
#             "cos smi" : cos smi value             }  da el table el wa7da 
#   "docID": [ {""} ]
#   "docID": [ {""} ]
# }

# positional_index = {
#   "term": [docfreq, {"docID": [postions]}, {"docID": [postions]}]
# }

#[{1: ['doc', 'number', '1', 'test']}, {2: ['doc', 'number', '2', 'test']}, {3: ['amr', 'bad', 'boy']}]

def initialize_vsm(dictionary_cutter):
    vsm = {}
    map(fun,dictionary_cutter)

    print(vsm)

