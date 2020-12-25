# positional_index = {
#   "term": [docfreq, {"docID": [postions]}, {"docID": [postions]}],
#   "term": [docfreq, {"docID": [postions]}, {"docID": [postions]}]
# }
#
import stopwords


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


def difference_between_two_arrays(first_document_positions, second_document_positions):
    # We loop through second list
    for second_pos in second_document_positions:
        for first_pos in first_document_positions:
            # if element in second list is less than first list, then break and catch the next element in second list
            if second_pos < first_pos:
                break
            # if element in second list is equal to first list, break and catch the next one
            if second_pos == first_pos:
                break
            # if none of the above and the difference between elements positions are one, return true as match is found
            if(second_pos - first_pos == 1):
                return True
    return False


# occurrence object = [{doc_id:[positions]}]
def compare_two_term_occurrences(first_term_occurrences, second_term_occurrences):
    result = []
    for first_occurence in first_term_occurrences:
        for first_document_id, first_document_positions in first_occurence.items():
            for second_occurence in second_term_occurrences:
                for second_document_id, second_document_positions in second_occurence.items():
                    if(first_document_id == second_document_id):
                        found = difference_between_two_arrays(
                            first_document_positions, second_document_positions)
                        if(found):
                            result.append(first_document_id)
    return result

# [1,3,5,8]
# [2,6,7]

# print(compare_two_term_occurrences(
#         [{1:[1,3,6]}, {2:[4, 5, 10, 15]}, {3: [4,6,7]}],
#         [{1:[1, 3, 4, 5]}, {3: [3,4,5,6]}]))
# print(compare_two_term_occurrences([{1:[1,3,6]}], [{1:[1, 4, 5, 6, 7]}]))


def find_term_occurrences_in_positional_index(term, positional_index):
    for positional_index_term, occurences in positional_index.items():
        if term == positional_index_term:
            # Here we are making a copy of the list to not affect the original list
            occurences_copy = occurences.copy()
            del occurences_copy[0]
            return occurences_copy
    return []

# positional_index = {
#   "term": [docfreq, {"docID": [postions]}, {"docID": [postions]}]
# }
#
# returns doc ids if match found


def phrase_query(query, positional_index):
    # tokenize query, remove stopwords
    tokens = query.split(' ')
    tokens = stopwords.extract_stopwords(tokens)
    tokens = [word.replace('.', '') for word in tokens]
    tokens = [word.replace(',', '') for word in tokens]
    tokens = [word.strip().lower() for word in tokens]

    result = []
    first_occurrences = []
    second_occurrences = []

    # Loop through terms in query
    for index, term in enumerate(tokens):
        # Find first term occurrences
        first_occurrences = find_term_occurrences_in_positional_index(
            term, positional_index)
        # check if occurrences found or not, if not found skip to next term
        if not first_occurrences:
            continue
        # if found occurrences catch the second term and find its occurrences
        # print(tokens[index+1])
        if (index + 1) == len(tokens):
            break
        next_term = tokens[index+1]
        second_occurrences = find_term_occurrences_in_positional_index(
            next_term, positional_index)
        # if second occurrences not found , reset first occurrences and start over
        if not second_occurrences:
            first_occurrences = []
            continue
        # if second occurrences found, compare both occurrences
        res = compare_two_term_occurrences(
            first_occurrences, second_occurrences)
        # if no result found, skip and continue
        if not res:
            continue
        # if result found return result
        result.append(res)
        # Returning this way to remove the arrays
    return [doc[0] for doc in result]
