# Contig Generation Problem

from itertools import product
import copy

arrow = ['1 -> 2',
'2 -> 3',
'3 -> 4,5',
'6 -> 7',
'7 -> 6',]

Patterns = ["ATG",
"ATG",
"TGT",
"TGG",
"CAT",
"GGA",
"GAT",
"AGA"]

GraphDic = dict((line.strip().split(' -> ') for line in arrow))

def debruijn_from_kmer(kmers):
    '''
    Construct the de Bruijn graph from a set of k-mers.
    Input: A collection of k-mers Patterns.
    Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).
    '''
    g = []
    # build a prefixing pattern dict
    dprefix = {}
    for e in kmers:
        prefix = e[:-1]
        dprefix.setdefault(prefix, []).append(e[1:])
    # build lexicographically sorted adjacency list
    for k in sorted(dprefix.keys()):
        g.append((k, sorted(dprefix[k])))
    return g


def in_and_out_degree(adjacency_list):
    '''
    return the in and out degree lists for a given graph's adjacency list
    '''
    ind = {}
    outd = {}
    for (k, v) in adjacency_list:
        outd[k] = len(v)
        for kk in v:
            ind[kk] = ind.get(kk, 0) + 1
    return (ind, outd)


def nearly_balanced(adjacency_list):
    '''
    return edge that will balance perfectly
    given graph assumed to be nearly balanced
    Input : nearly balanced graph
    Output :
    balancing_edge
    '''
    (ind, outd) = in_and_out_degree(adjacency_list)
    end = [(k, v - outd.get(k, 0)) for k, v in ind.iteritems() if v > outd.get(k, 0)]
    beg = [(k, v - ind.get(k, 0)) for k, v in outd.iteritems() if v > ind.get(k, 0)]
    if (len(end) == 1) and (end[0][1] == 1) and \
            (len(beg) == 1) and (beg[0][1] == 1):
        return (end[0][0], beg[0][0])
    return None



def maximal_non_branching_paths(adjacency_list):
    '''
    Implement MaximalNonBranchingPaths.
    Input: The adjacency list of a graph whose nodes are integers.
    Output: The collection of all maximal nonbranching paths in this graph.
    '''
    dadj = {}
    for (k, v) in adjacency_list:
        dadj[k] = dadj.get(k, []) + v[:]
    degree = in_and_out_degree(adjacency_list)
    paths = []

    def is_one_in_one_out(vertex):
        deg_in = degree[0].get(vertex, 0)
        deg_out = degree[1].get(vertex, 0)
        return (deg_in == 1) and (deg_out == 1)

    def visited(vertex):
        # linear time visited-vertex implementation
        # fixme : use dict to get constant time
        for path in paths:
            if vertex in path:
                return True
        return False

    def isolated_cycle(vertex):
        '''
        return isolated cycle including vertex v if any
        '''
        cycle = [vertex]
        while is_one_in_one_out(cycle[-1]):
            cycle.append(dadj[cycle[-1]][0])
            if cycle[0] == cycle[-1]:
                return cycle
        return None

    def non_branching_path(edge):
        '''
        return the non-branching path starting with edge edge
        '''
        branch = edge[:]
        while is_one_in_one_out(branch[-1]):
            branch.append(dadj[branch[-1]][0])
        return branch

    for (v, e) in dadj.iteritems():
        #        # cut-off optimization, skip v node if already in path list
        #        if visited(v) :
        #            continue
        deg_in = degree[0].get(v, 0)
        deg_out = degree[1].get(v, 0)
        if (deg_in == 1 and deg_out == 1):
            # vertex v is 1-in-1-out node
            # could be part of a new isolated cycle, check this...
            if not visited(v):
                cycle = isolated_cycle(v)
                if cycle:
                    paths.append(cycle)
        elif (deg_out > 0):
            # explore vertex v outgoing branches
            for w in e:
                paths.append(non_branching_path([v, w]))
    return paths


def genome_path(path):
    return ''.join([e[0] for e in path]) + path[-1][1:]

def contigs_from_reads(kmers):
    '''
    Generate the contigs from a collection of reads (with imperfect coverage).
    Input: A collection of k-mers Patterns.
    Output: All contigs in DeBruijn(Patterns).
    '''
    g = debruijn_from_kmer(kmers)
    m = maximal_non_branching_paths(g)
    return sorted(map(genome_path, m))


print(debruijn_from_kmer(Patterns))
print(contigs_from_reads(Patterns))