from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))


def extract_stopwords(tokens_list):
    filtered_list = []
    for token in tokens_list:
        if token not in stop_words:
            filtered_list.append(token)
    return filtered_list
