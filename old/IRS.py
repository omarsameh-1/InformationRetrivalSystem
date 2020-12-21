from os import path
import pathlib


def Tokens(PathFolder):
    theList=[]
    for line in PathFolder:
        for p in "!.,:@#$%^&?<>*()[}{]-=;/\"\\\t\n":
            if p in '\n;?:!.,.':
                line = line.replace(p,' ')
            else: line = line.replace(p,'')
        for word in line.split():
            theList.append(word.strip().lower())
    return theList




print(list(GetTokensInDoc()))#Success Test
#Note:-> C:\\Users\\amrahmed\\Desktop\\IR\\Documents
