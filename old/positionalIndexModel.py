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