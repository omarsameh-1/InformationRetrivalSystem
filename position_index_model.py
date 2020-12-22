# positional_index = {
#   "term": [docfreq, {"docID": [postions]}, {"docID": [postions]}],
#   "term": [docfreq, {"docID": [postions]}, {"docID": [postions]}]
# }
#

def initialize_posting_list(tokens_list):
    posting_list = {}
    for token in tokens_list:
        posting_list[token] = []
    return posting_list


def get_positions_in_doc(term, doc):
    positions = [i + 1 for i, t in enumerate(doc) if t == term]
    return positions


def calc_term_frequency(term, doc):
    return len(get_positions_in_doc(term, doc))


def construct_positional_index(main_dictionary, tokens_list):
    positional_index = initialize_posting_list(tokens_list)
    for term in tokens_list:
        for dictionary in main_dictionary:
            for doc_id, tokens in dictionary.items():
                # check if term is occuring in this doc
                # if it is occuring, get positions and return object {doc_id: [positions]}
                # and append this object to the positional index model corresponding term
                term_positions = get_positions_in_doc(term, tokens)
                if not term_positions:
                    continue
                obj = {doc_id: term_positions}
                positional_index[term].append(obj)
        # get doc frequency by getting length and insert it to the beginning of list
        doc_frequency = len(positional_index[term])
        positional_index[term].insert(0, doc_frequency)
    return positional_index
