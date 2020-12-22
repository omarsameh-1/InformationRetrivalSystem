import numpy as np
import IRSmodified

def constructePositionalIndexM(Ts,listOfDics):
    valuesWP={}
    positionsL=[]
    positionalIndexM={}
    for Term in Ts:
         
        for Dic in listOfDics:
            Vs=Dic.values()
            k=list(Dic.keys())
            for value in Vs:
                i=0
                if Term in value:
                    #print(Term,k[0],"\n")
                    positionsL.append(i)
                    valuesWP[k[0]]=positionsL
                    K2=[Term,len(valuesWP)]
                    positionalIndexM[Term,len(valuesWP)]=valuesWP
                    i=i+1
    return positionalIndexM

print(constructePositionalIndexM(IRSmodified.Ts,IRSmodified.ff))

# C:\\Users\\sata\\Desktop\\oppd



# def constructePositionalIndexM(listOfAllTerm, GetTokensInDoc):
#     pList = []
#     pDic = {}
#     terDic = {}
#     tList = []
#     ffList = []
#     docID = 0
#     for Term in ts:
#         tList.clear()
#         for i in f:
#             pList.clear()
#             for key, vals in i.items():
#                 vList = list(vals)
#                 for val in vList:
#                     if Term == val:
#                         docID = key
#                         pList.append(vList.index(val))
#             if pList:
#                 pDic = {docID: pList}
#                 print(Term, ":", pDic)