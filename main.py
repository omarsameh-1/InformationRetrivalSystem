import tokenization
import position_index_model

dictionary = tokenization.get_tokens_list()
# print(dictionary)

dictionary_cutter = tokenization.cutter(dictionary)
# print(dictionary)

removed = tokenization.remove_duplicates_from_dictionary(dictionary_cutter)
# print(removed)

posting_list = position_index_model.initialize_posting_list(removed)
# print(posting_list)

position_index_model.construct_positional_index(dictionary, removed)