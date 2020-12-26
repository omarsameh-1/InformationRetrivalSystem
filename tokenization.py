import pathlib
from os import path
from stopwords import extract_stopwords


def tokenize(file):
    the_list = []
    for line in file:
        line = line.replace('.', '')
        line = line.replace(',', '')
        for word in line.split():
            the_list.append(word.strip().lower())
    return the_list


def tokenize_and_remove_duplicates(file):
    the_list = set()
    for line in file:
        line = line.replace('.', '')
        line = line.replace(',', '')
        for word in line.split():
            the_list.add(word.strip().lower())
    return list(the_list)


def get_list(dictionary):
    our_list = []
    for key in dictionary.keys():
        our_list.append(key)
    return our_list


def get_path():
    #filePath = '/run/media/DATA/All/Projects/information-retrieval-system/documents/'
    filePath = input("FilePath= ")
    file_path = path.relpath(filePath)
    return file_path


def get_tokens_list():
    dictionary = {}
    dictionaries_list = []
    tokens_list = []
    doc_id = 1
    folder_path = get_path()
    for path in pathlib.Path(folder_path).iterdir():
        if path.is_file():
            current_file = open(path, "r")
        tokens_list = tokenize(current_file)
        tokens_list = extract_stopwords(tokens_list)
        if not tokens_list:
            continue
        dictionary = {doc_id: tokens_list}
        doc_id += 1
        dictionaries_list.append(dictionary.copy())
    return dictionaries_list


def remove_duplicates_from_dictionary(dictionary):
    list_of_terms = set()
    for dic in dictionary:
        vs = dic.values()
        for Term in vs:
            list_of_terms.add(Term)
    return list(list_of_terms)


def cutter(dictionary_list):
    i, fList = 0, []
    for dic in dictionary_list:
        values = dic.values()
        keys = list(dic.keys())
        for value in values:
            for terms in value:
                fList.append({keys[i]: terms})
    i = i + 1
    return fList
