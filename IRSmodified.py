from os import path
import pathlib


thedic = {}
def Tokens(PathFolder):
    theList=[]
    for line in PathFolder:
        line = line.replace('.','')
        line = line.replace(',','')
        for word in line.split():
            theList.append(word.strip().lower())
    return theList


def TokensWithoutDublication(PathFolder):
    theList=set()
    for line in PathFolder:
        line = line.replace('.','')
        line = line.replace(',','')
        for word in line.split():
          theList.add(word.strip().lower())

    return list(theList)

def getList(dict): 
    list = [] 
    for key in dict.keys(): 
        list.append(key) 
          
    return list

Note = r"you must edit ur file path from  \ to \\"
print(Note)
def getPath():
    filePath = input("FilePath= ")
    file_path = path.relpath(filePath)
    return file_path


cheDicEm= not bool(thedic)
def GetFList():
    firstID=0  
    finaList=[]
    List_Token=[]
    Knum=firstID
    f=getPath()
    for path in pathlib.Path(f).iterdir():
        if path.is_file():
            current_file = open(path, "r")
        List_Token=Tokens(current_file)
        if str(cheDicEm) == True:
            thedic={firstID:List_Token}
        else:  
            Knum=Knum +1
            thedic={Knum:List_Token}
        finaList.append(thedic.copy())
    return finaList


def GetFListWoDublicaton():
    firstID=0  
    finaList=[]
    List_Token=[]
    Knum=firstID
    f=getPath()
    for path in pathlib.Path(f).iterdir():
        if path.is_file():
            current_file = open(path, "r")
        List_Token=TokensWithoutDublication(current_file)
        if str(cheDicEm) == True:
            thedic={firstID:List_Token}
        else:  
            Knum=Knum +1
            thedic={Knum:List_Token}
        finaList.append(thedic.copy())
    return finaList

ff=[]
ff=GetFList()
# TermsWDid=[]
# TermsWDid=GetFListWoDublicaton()

def cutter (listOfDic):
    i,fList=0,[]
    for dic in listOfDic:
        vs=dic.values()
        ks=list(dic.keys())
        for value in vs:
            for terms in value:
                fList.append({ks[i]:terms})
    i=i+1
    return fList    

TermsAsDics=cutter(ff)
print(TermsAsDics)

def ListOfAllTerms(TermsAsDic):
    listOfAllT=set()
    for dic in TermsAsDic:
        vs=dic.values()
        for Term in vs:
            listOfAllT.add(Term)
    return list(listOfAllT)

Ts=[]
Ts=ListOfAllTerms(TermsAsDics)

# print(f"Ts= {Ts}")
# print("\n")
# print(f"TermsWDid= {ff}")
        



# p=['lgre','rkijir','gjknlk','jggrr','jnnolr','rkllnlgw']
# c=[{1:['dkn','lgre']},{2:['ekfe','jnnolr']},{4:['ker','jknnreg','kjww']}]
# for term in p:
#     #print(term)
#     for terms in c:
#         #print(terms)
#         vs=terms.values()
#         k=list(terms.keys())
#         for value in vs:
#             #print(value)
#             if term in value:
#                 print (k[0])



