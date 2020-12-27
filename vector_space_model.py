import numpy as np
import math as m
from numpy.core.defchararray import array
import tokenization as tk

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


def calc_document_length(TFidfs_of_document):
    return np.linalg.norm(array(TFidfs_of_document))


'''this function take TFidf of a term in a spacific document 
    and the length of that spacific document and returns the normlize_TFidf'''


def calc_normalize_TFidf(term_TFidf, document_length):
    return term_TFidf/document_length


'''this fucntion takes a list of the normlize TFidf of all terms 
    in a spacific document and a list the normlize TFidf of all terms 
    in the query and return "the score for that spacific document"=(similiraty
    between that document and the query)'''

# doc normalized list = [0.67 , 0.511 , 0 , 0.53]
# query normalized list = [0 , 0 , 0.768 , 0.680]
# cos simi = 0.36


def calc_similarity(normalize_TFidfs_of_document, normalize_TFidfs_of_query):
    return (np.dot(normalize_TFidfs_of_document, normalize_TFidfs_of_query))


# positional_index = {
#   "term": [docfreq, {"docID": [postions]}, {"docID": [postions]}]
# }

#[{1: ['doc', 'number', '1', 'test']}, {2: ['doc', 'number', '2', 'test']}, {3: ['amr', 'bad', 'boy']}]

# Returns vsm = {
#   "doc_id": {"terms" : [
#       {"term1": []},
#       {"term2": []}
#   ]}
# }
def initialize_vsm(dictionary_cutter):
    vsm = {}
    # Loop through the dictionary we recieved and catch each doc
    for doc in dictionary_cutter:
        # we have doc_id and its terms
        for doc_id, terms in doc.items():
            # check if doc_id already exists in the vsm
            # if it exists append the term to the terms list
            if doc_id in vsm.keys():
                vsm[doc_id]['terms'].append({terms: {}})
            # if it doesn't exist, create new doc and initialize it
            else:
                vsm[doc_id] = {"terms": [{terms: {}}]}
    return vsm

# vector_space_model = {
#   "docID": {"terms" :[{"term1" : {termfreq , tfw , idf , tfidf , normalize Tfidf}}
#                       {"term2" : {termfreq , tfw , idf , tfidf , normalize Tfidf}}
#                      ],
#             "docLength" : doclengthvalue,
#             "cos smi" : cos smi value
#           }  da el table el wa7da
# }


def construct_vsm(dictionary_cutter, positional_index):
    initial_vsm = initialize_vsm(dictionary_cutter)
    # Loop through the initial vsm and addvalues like term_frequency, tfw, idf, tfidf, normalize_tfidf to each term
    # catching each doc and its object containing its details

    for doc_id, obj in initial_vsm.items():
        tfidfs_of_doc = []
        # we now have the terms key and terms list
        for key, items_list in obj.items():
            # we catch each term in the doc
            for term in items_list:
                # we now catch each term and its properties and add them as needed
                for term, props in term.items():
                    # function made to abstract the setting props part
                    set_term_props(doc_id, term, props, positional_index[term])
                    tfidfs_of_doc.append(props["tfidf"])
        obj["doc_length"] = calc_document_length(tfidfs_of_doc)
        # obj["cosine_similarity"] = "cosine similarity value"
        for key, items_list in obj.items():
            if key == "terms":
                for term in items_list:
                    for term, props in term.items():
                        props["normalize_tfidf"] = calc_normalize_TFidf(props["tfidf"], obj["doc_length"])
    return initial_vsm


# Function to fill each term's props
def set_term_props(doc_id, term, props, term_pi):
    # retrieve all docs with their tokens
    tokens = tk.get_tokens_list()
    term_frequency = 0
    number_of_docs = len(tokens)

    for doc in tokens:
        for id, tokens_list in doc.items():
            if id == doc_id:
                for token in tokens_list:
                    if token == term:
                        term_frequency += 1

    document_frequency = term_pi[0]
    term_frequency_weight = calc_term_frequency_weight(term_frequency)
    idf = calc_idf(number_of_docs, document_frequency)
    tfidf = calc_term_TFidf(term_frequency_weight, idf)

    props["term_frequency"] = term_frequency
    props["tfw"] = term_frequency_weight
    props["idf"] = idf
    props["tfidf"] = tfidf
    return props


def search_vsm(query, vsm):
    result = []
    # LAST THING TO DO

    return result
