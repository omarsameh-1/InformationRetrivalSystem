# we try to build a structure of Postional Index Like that: [ { Term:[termFreq,{docID:[Postions] } ] } ]
# i also let it here
def constructePositionalIndexM(listOfAllTerm, GetTokensInDoc):
    pList = []
    pDic = {}
    terDic = {}
    tList = []
    ffList = []
    docID = 0
    for Term in ts:
        tList.clear()
        for i in f:
            pList.clear()
            for key, vals in i.items():
                vList = list(vals)
                for val in vList:
                    if Term == val:
                        docID = key
                        pList.append(vList.index(val))
            if pList:
                pDic = {docID: pList}
                print(Term, ":", pDic)


# PIN = {
#     "term": [docfreq, [{"docID": [postions]}, {"docID": [postions]}]],
#     "term": [docfreq, {"docID": [postions]}, {"docID": [postions]}]
# }


# def get_key(dict, val):
#     for key, value in dict.items():
#         if val == value:
#             return key
#     return "key doesn't exist"

# #
# Fetch the document.
# Remove stop words, stem the resulting words.
# If the word is already present in the dictionary, add the document and the corresponding positions it appears in. Else, create a new entry.
# Also update the freqency of the word for each document, as well as the no. of documents it appears in.
#


def initialize_posting_list(tokens_list):
    posting_list = {}
    for token in tokens_list:
        posting_list[token] = [0]
    return posting_list


def construct_positional_index(main_dictionary, tokens_list):
    positional_index = initialize_posting_list(tokens_list)
    for term in tokens_list:
        list_entry = {}
        term_name = ""
        doc_frequency = 0
        positions = []

        for doc_id, tokens in main_dictionary:
            print("Doc Id: " + doc_id + " tokens: " + tokens)
            # for token in tokens:
            #     if term == token:
            #         list_entry[term] = []
    return positional_index
