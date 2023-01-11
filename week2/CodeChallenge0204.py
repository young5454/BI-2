k = int(input('Enter k:' ))
import math

def generate_binary(n):
    bin_list = []
    bin_str = [0] * n

    for i in range(0, int(math.pow(2, n))):

        bin_list.append("".join(map(str, bin_str))[::-1])
        bin_str[0] += 1

        # Iterate through entire array if there carrying
        for j in range(0, len(bin_str) - 1):

            if bin_str[j] == 2:
                bin_str[j] = 0
                bin_str[j + 1] += 1
                continue

            else:
                break

    return bin_list


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
    #for keys in adjDic.keys():
        #joined_string = ",".join(adjDic[keys])
        #print(keys + " -> " + joined_string)
    return adjDic

def Prefix(Pattern):
    k = len(Pattern)
    return Pattern[0:k-1]

def Suffix(Pattern):
    k = len(Pattern)
    return Pattern[1:k]

def NewCycle(list):
    n = len(list)
    return list[:n-1]

def PathToGenome(path):
    # path is a list

    FirstSequence = path[0]
    n = len(path)
    k = len(FirstSequence)
    for i in range(1, n):
        FirstSequence = FirstSequence + path[i][k - 1]
    return FirstSequence

def GetUniversalString(k):
    patterns = generate_binary(k)
    dB = DeBrujin(patterns)
    #print(dB)
    euleriancycle = EulerianCycle(dB)
    newcycle = NewCycle(euleriancycle)
    universalstring = PathToGenome(newcycle)
    n = len(universalstring)
    finaluniversalstring = universalstring[:n-k+2]
    #print(euleriancycle)
    #print(newcycle)
    #print(universalstring)
    return finaluniversalstring

print(GetUniversalString(k))
