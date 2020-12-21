from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
# list of tokens
# dummy list for test purposes 
# tokens = ['this', 'is', 'an', 'example', 'sentence', 'for', 'testing']


def extract_stopwords(tokens_list):
    filtered_list = []
    for token in tokens_list:
        if token not in stop_words:
            filtered_list.append(token)
    return filtered_list


# filtered = extract_stopwords(tokens)
# print(filtered)
