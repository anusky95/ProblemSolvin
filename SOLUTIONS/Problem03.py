from collections import OrderedDict
def alphadictionary(testString):
    testString = testString.lower()
    resultDict=OrderedDict()
    nonalpha=[]
    for i in testString:
        if (i.isalpha())==False:
            nonalpha.append(i)
        else:
            resultDict[i] = resultDict.get(i,0)+1
    resultDict['etc']=len(nonalpha)
    print("{")
    for k,v in resultDict.items():
        print("%s : %d," % (k,v))
    print("}")

def main():
    
    stra = str(input())
    alphadictionary(stra)

if __name__ == '__main__':
    main()
