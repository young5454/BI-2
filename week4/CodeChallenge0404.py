# Spectral Convolution Problem
import operator
from copy import deepcopy

spectrum = []
with open('dataset_104_4.txt') as file:
    for line in file:
        spectrum += line.rstrip().split()
    spectrum = [int(x) for x in spectrum]
    spectrum.sort()


spectrumo = [57, 57, 71, 99, 129, 137, 170, 186, 194, 208, 228, 265, 285, 299, 307, 323, 356, 364, 394, 422, 493]

def Convolution(Spectrum):
    ConvolutionList = []
    n = len(Spectrum)
    i = 0
    while i < n:
        for j in range(i+1, n):
            cha = Spectrum[j] - Spectrum[i]
            ConvolutionList.append(cha)
        i = i + 1
    for value in ConvolutionList:
        if value == 0:
         ConvolutionList.remove(value)
    ConvolutionList.sort()
    return ConvolutionList

M = 17

def ConvolutionFrequency(convolutionlist):
    ConDic = {}
    ConSet = frozenset(convolutionlist)
    for item in ConSet:
        if 57 <= item <= 200:
            ConDic[item] = convolutionlist.count(item)
    SortedConDic = dict(sorted(ConDic.items(), key=operator.itemgetter(1), reverse=True))
    copy = deepcopy(SortedConDic)
    values = list(SortedConDic.values())
    # take only value between 57 and 200
    cut = values[M - 1]
    for key in SortedConDic.keys():
        if SortedConDic[key] < cut:
            del copy[key]
    candidate = list(copy.keys())
    candidate.sort()
    return candidate

# Implement ConvolutionCyclopeptideSequencing.

Convolutionlist = Convolution(spectrumo)
result = ConvolutionFrequency(Convolutionlist)
print(*result)
