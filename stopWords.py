import nltk 
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))  
 # list of stop words
# stopWordLst = ['and','or','the','this','there','that','these','they','are','of','to','a','an','for','have'
# ,'has']
# list of tokens
# dummy list for test purposes 
tokensLst = ['this','is','an','example','sentence','for','testing']
# list free of stop words
filterdLst = []


def stopFunction (tokensLst):
    for i in tokensLst:
        if i not in stop_words:
            filterdLst.append(i)
    return filterdLst


stopFunction(tokensLst)
print(filterdLst)

