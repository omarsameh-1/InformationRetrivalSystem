import tokenization
import position_index_model as pi

dictionary = tokenization.get_tokens_list()
# print(dictionary)

dictionary_cutter = tokenization.cutter(dictionary)
# print(dictionary)

tokens_without_duplicates = tokenization.remove_duplicates_from_dictionary(
    dictionary_cutter)
# print(removed)

posting_list = pi.initialize_posting_list(tokens_without_duplicates)
# print(posting_list)

positional_index = pi.construct_positional_index(
    dictionary, tokens_without_duplicates)

# print(positional_index)

res = pi.phrase_query('amr is a bad number 2', positional_index)
res.sort()
print(res)
