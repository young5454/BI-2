# (k, d)-mer Generating Problem
# String Reconstruction from Read-Pairs Problem

k = int(input('Enter k: '))
d = int(input('Enter d: '))
Text = 'TAATGCCATGGGATGTT'
pair = 'AAT|CAT'

GappedPatterns = open('Test').read().split()

GappedPatternsy = ['GAGA|TTGA',
'TCGT|GATG',
'CGTG|ATGT',
'TGGT|TGAG',
'GTGA|TGTT',
'GTGG|GTGA',
'TGAG|GTTG',
'GGTC|GAGA',
'GTCG|AGAT']

GappedPatternsx = ['ACC|ATA',
'ACT|ATT',
'ATA|TGA',
'ATT|TGA',
'CAC|GAT',
'CCG|TAC',
'CGA|ACT',
'CTG|AGC',
'CTG|TTC',
'GAA|CTT',
'GAT|CTG',
'GAT|CTG',
'TAC|GAT',
'TCT|AAG',
'TGA|GCT',
'TGA|TCT',
'TTC|GAA']

def PairedComposition(k, d, Text):
    # returns a kmer composing Text in lexicographic order

    KmerList = []
    n = len(Text)
    for i in range(n-2*k-d+1):
        window1 = Text[i:i+k]
        window2 = Text[i+k+d:i+d+2*k]
        KmerList.append(window1 + '|' + window2)
    KmerList.sort()
    return KmerList

#print(PairedComposition(k, d, Text))


def PairedSuffix(k, d, pair):
    n = len(pair) # 2k + 1
    window1_suffix = pair[1:k]
    window2_suffix = pair[k+2: n]
    suffix = window1_suffix + '|' + window2_suffix
    return suffix
    #print(window1, window2)

def PairedPrefix(k, d, pair):
    n = len(pair)  # 2k + 1
    window1_prefix = pair[:k-1]
    window2_prefix = pair[k+1: n-1]
    prefix = window1_prefix + '|' + window2_prefix
    return prefix
    # print(window1, window2)


# String Spelled by a Gapped Genome Path Problem
def StringSpelledByGappedPatterns(k, d, GappedPatterns):
    FirstPatterns = []
    SecondPatterns = []
    for Text in GappedPatterns:
        FirstPatterns.append(Text[:k])
        SecondPatterns.append(Text[k+1:2*k+1])
    PrefixStirng = PathToGenome(FirstPatterns)
    SuffixString = PathToGenome(SecondPatterns)

    n = len(PrefixStirng)
    for j in range(k+d+1, n):
        if PrefixStirng[j] != SuffixString[j-k-1-d]:
            return "there is no string spelled by the gapped patterns"
    Final = PrefixStirng + SuffixString[n-k-1-d:n]

    return Final

def PathToGenome(path):
    # path is a list

    FirstSequence = path[0]
    n = len(path)
    k = len(FirstSequence)
    for i in range(1,n):
        FirstSequence = FirstSequence + path[i][k-1]
    return FirstSequence

def PairedDeBrujin(Patterns):
    nodes = []
    for Kmer in Patterns:
        nodes.append(PairedPrefix(k, d, Kmer))
    nodes.sort()
    adjDic = {}
    for node in nodes:
        dummylist = []
        for Kmer in Patterns:
            prefix = PairedPrefix(k, d, Kmer)
            if node == prefix:
                dummylist.append(PairedSuffix(k, d, Kmer))
                adjDic[node] = dummylist
    #for keys in adjDic.keys():
        #joined_string = ",".join(adjDic[keys])
        #print(keys + " -> " + joined_string)
    return adjDic

def EulerianCycle(edge_dict):
    # set the first node to to 0th node in NodesList
    # path is a small loop consisting the overall cycle
    NodesList = []
    for key in edge_dict.keys():
        NodesList.append(key)

    current_node = NodesList[0]
    path = [current_node]

    # make the first path
    while True:
        path.append(edge_dict[current_node][0])

        if len(edge_dict[current_node]) == 1:
            # delete the node from dictionary if no more neighbors are available
            del edge_dict[current_node]
        else:
            # if there are more left
            edge_dict[current_node] = edge_dict[current_node][1:]

        if path[-1] in edge_dict:
            # the last node from path
            current_node = path[-1]
        else:
            break

    # continue and add loops until dictionary = 0
    # if there are non left, the overall Eulerian cycle will be returned

    while len(edge_dict) > 0:
        for i in range(len(path)):
            if path[i] in edge_dict:
                current_node = path[i]
                cycle = [current_node]
                while True:
                    cycle.append(edge_dict[current_node][0])

                    if len(edge_dict[current_node]) == 1:
                        del edge_dict[current_node]
                    else:
                        edge_dict[current_node] = edge_dict[current_node][1:]

                    if cycle[-1] in edge_dict:
                        current_node = cycle[-1]
                    else:
                        break

                path = path[:i] + cycle + path[i+1:]
                break
    return path

def NodeList(dict):
    node_list = []
    for key in dict.keys():
        node_list.append(key)
    for valuelist in dict.values():
        for value in valuelist:
            node_list.append(value)
    node_list = set(node_list)
    return node_list

def OutDegreeCount(dict):
    outdegreedic = {}
    for key in dict.keys():
        outdegreedic[key] = len(dict[key])
    return outdegreedic

def InDegreeCount(dict):
    indegreedic = {}
    valuelist = []
    for value in dict.values():
        valuelist = valuelist + value
    for key in NodeList(dict):
        indegreedic[key] = valuelist.count(key)
    return indegreedic

def SumDegreeCount(dict):
    outdegreedic = OutDegreeCount(dict)
    indegreedic = InDegreeCount(dict)
    sumdegreedic = {}
    for key in outdegreedic.keys():
        sum = outdegreedic[key] + indegreedic[key]
        sumdegreedic[key] = sum
    return sumdegreedic

def GetStart(dict):
    nodelist = NodeList(dict)
    indegree = InDegreeCount(dict)
    outdegree = OutDegreeCount(dict)
    for node in outdegree.keys():
        if node not in indegree.keys() or indegree[node] < outdegree[node]:
            return node

def GetEnd(dict):
    nodelist = NodeList(dict)
    indegree = InDegreeCount(dict)
    outdegree = OutDegreeCount(dict)
    for node in nodelist:
        if node not in outdegree.keys() or indegree[node] > outdegree[node]:
            return node

def EulerianPath(edge_dict):
    # get starting, ending node
    end_node = GetEnd(edge_dict)
    start_node = GetStart(edge_dict)

    if end_node in edge_dict:
        edge_dict[end_node].append(start_node)
    else:
        edge_dict[end_node] = [start_node]

    cycle = EulerianCycle(edge_dict)
    n = len(cycle)
    for i in range(n):
        if cycle[i:i+2] == [end_node, start_node]:
            divide_point = i
    # reassemble order
    #return cycle
    return cycle[divide_point+1:]+cycle[1:divide_point+1]


dict = PairedDeBrujin(GappedPatterns)
Pathed_Patterns = EulerianPath(dict)
l = k-1
print(StringSpelledByGappedPatterns(l, d, Pathed_Patterns))
