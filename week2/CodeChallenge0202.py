# Eulerian Path Problem

with open('input.txt', 'r') as file:
    GraphDic = dict((line.strip().split(' -> ') for line in file))
    for key in GraphDic:
        GraphDic[key] = GraphDic[key].split(',')

NodesList = []
for key in GraphDic.keys():
    NodesList.append(key)

def EulerianCycle(edge_dict):
    # set the first node to to 0th node in NodesList
    # path is a small loop consisting the overall cycle

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


def EulerianPathOutputFormat(eulerianpath):
    n = len(eulerianpath)
    j = 0
    output = ''
    while j < n-1:
        output = output + eulerianpath[j] + '->'
        j = j + 1
    output = output + eulerianpath[-1]
    return output


eulerianpath = EulerianPath(GraphDic)
print(eulerianpath)
print(EulerianPathOutputFormat(eulerianpath))
