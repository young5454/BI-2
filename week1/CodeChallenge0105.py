# DeBruijn Graph from k-mers Problem

Patternsy = open('dataset_200_8 (1).txt').read().split()
Patterns = [
"GAGG",
"CAGG",
"GGGG",
"GGGA",
"CAGG",
"AGGG",
"GGAG"
]

def DeBrujin(Patterns):

    nodes = []
    for Kmer in Patterns:
        nodes.append(Prefix(Kmer))
    nodes.sort()
    adjDic = {}
    for node in nodes:
        dummylist = []
        for Kmer in Patterns:
            prefix = Prefix(Kmer)
            if node == prefix:
                dummylist.append(Suffix(Kmer))
                adjDic[node] = dummylist
    for keys in adjDic.keys():
        joined_string = ",".join(adjDic[keys])
        print(keys + " -> " + joined_string)


def Composition(k, Text):
    # returns a kmer composing Text in lexicographic order w/ duplicates

    KmerList = []
    n = len(Text)
    for i in range(n-k+1):
        window = Text[i:i+k]
        KmerList.append(window)
    KmerList.sort()
    return KmerList


def DeBrujinNodes(k, Text):
    # returns a k-1 mer (Debrujin nodes)
    # composing Text in lexicographic order w/o duplicates

    KmerSet = set()
    n = len(Text)
    for i in range(n-k+1):
        window = Text[i:i+k-1]
        KmerSet.add(window)
    Nodes = list(KmerSet)
    Nodes.sort()
    return Nodes


def Prefix(Pattern):
    k = len(Pattern)
    return Pattern[0:k-1]


def Suffix(Pattern):
    k = len(Pattern)
    return Pattern[1:k]


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


print(DeBrujin(Patternsy))
