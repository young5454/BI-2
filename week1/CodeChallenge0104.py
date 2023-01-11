# De Bruijn Graph from a String Problem
k = int(input('Enter k: '))
Text = input('Enter Text: ')

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

def DeBrujin(k, Text):
    # string into Pattern
    nodes = DeBrujinNodes(k, Text)
    allKmers = Composition(k, Text)
    adjDic = {}
    for node in nodes:
        dummylist = []
        for Kmer in allKmers:
            prefix = Prefix(Kmer)
            if node == prefix:
                dummylist.append(Suffix(Kmer))
                adjDic[node] = dummylist
    for keys in adjDic.keys():
        joined_string = ",".join(adjDic[keys])
        print(keys + " -> " + joined_string)







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


def Overlap(k, Text):
    dic = {}
    nodes = DeBrujinNodes(k, Text)
    allKmers = Composition(k, Text)
    n = len(nodes)
    for node in nodes:
        pattern_list = []
        for Kmers in allKmers:
            suffix = Suffix(Kmers)
            if node == suffix:
                pattern_list.append(suffix)
                dic[node] = pattern_list
    for keys in dic.keys():
        joined_string = ",".join(dic[keys])
        print(keys + " -> " + joined_string)

print(DeBrujinNodes(k, Text))
print(Composition(k, Text))
print(DeBrujin(k, Text))