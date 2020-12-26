import vector_space_model as vsm 



def test_vsm():
    
    Tfw = vsm.calc_term_frequency_weight(10)
    if(Tfw == 2 and vsm.calc_term_frequency_weight(1) == 1  ):
        print("tfw is working")
    else :
        print("tfw not working ")

    idf = vsm.calc_idf(806791,6723)
    print(f"idf = {idf}")
    if(round(idf) == 2):
        print("idf is working")
    else: 
        print("idf NOT working")


    TfIdf= vsm.calc_term_TFidf(2,2)
    if(TfIdf == 4 ):
        print( "tfidf is working")
    else :
        print("tfidf is Not working")


## length fun takes ifdfs list 
    length= vsm.calc_document_length([0.584,0.584,0.584])
    print(length)
    if(length == 1.011 ):
        print( "length works pretty fine")
    else :
        print( "length is not working ")


#doc normalized list = [0.67 , 0.511 , 0 , 0.53]
# query normalized list = [0 , 0 , 0.768 , 0.680]
#cos simi = 0.36
    docList = [0.67 , 0.511 , 0 , 0.53] 
    queryList = [0 , 0 , 0.768 , 0.680]

    print(f" cos simi = {vsm.calc_similarity(docList,queryList)}")
    if(vsm.calc_similarity(docList,queryList) == 0.36 ):
        print("tfd is working")



test_vsm()