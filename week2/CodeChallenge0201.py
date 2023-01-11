# Eulerian Cycle Problem

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


def EulerianCycleOutputFormat(euleriancycle):
    n = len(euleriancycle)
    j = 0
    output = ''
    while j < n-1:
        output = output + euleriancycle[j] + '->'
        j = j + 1
    output = output + euleriancycle[0]
    return output


euleriancycle = EulerianCycle(GraphDic)
print(EulerianCycleOutputFormat(euleriancycle))
