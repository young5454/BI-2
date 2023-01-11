# Cyclopeptide Scoring Problem

Peptide = 'PEEP'
Spectrumy = [0, 97, 129, 129, 129, 194, 226, 323, 323, 355, 452]

Alphabet = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N',
            'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']

Spectrum = []
with open('dataset_4913_1.txt') as file:
    for line in file:
        Spectrum += line.rstrip().split()
    Spectrum = [int(x) for x in Spectrum]


AminoAcidMass = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97,
    'V': 99, 'T': 101, 'C': 103, 'I': 113,
    'L': 113, 'N': 114, 'D': 115, 'K': 128,
    'Q': 128, 'E': 129, 'M': 131, 'H': 137,
    'F': 147, 'R': 156, 'Y': 163, 'W': 186}

def Pepweight(peptide):
    weight = 0
    for s in peptide:
        weight = weight + AminoAcidMass[s]
    return weight


def LinearSpectrum(Peptide, Alphabet, AminoAcidMass):
    n = len(Peptide)
    PrefixMass = []
    for i in range(n+1):
        window = Peptide[:i]
        window_weight = Pepweight(window)
        PrefixMass.append(window_weight)
    #return PrefixMass
    linearspectrum = [0]
    for i in range(n):
        for j in range(i+1, n+1):
            add = PrefixMass[j] - PrefixMass[i]
            linearspectrum.append(add)
    linearspectrum.sort()
    return linearspectrum


def CyclicSpectrum(Peptide, Alphabet, AminoAcidMass):
    n = len(Peptide)
    PrefixMass = []
    for i in range(n + 1):
        window = Peptide[:i]
        window_weight = Pepweight(window)
        PrefixMass.append(window_weight)
    peptideMass = PrefixMass[n]
    cyclicspectrum = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            add = PrefixMass[j] - PrefixMass[i]
            cyclicspectrum.append(add)
            if i>0 and j < n:
                lemon = peptideMass - (PrefixMass[j] - PrefixMass[i])
                cyclicspectrum.append(lemon)
    cyclicspectrum.sort()
    return cyclicspectrum


def Score(Peptide, Spectrum): #spectrum should be in list form
    IdealSpectrum = CyclicSpectrum(Peptide, Alphabet, AminoAcidMass)
    IdealSet = frozenset(IdealSpectrum)
    IdealDic = {}
    SpectrumSet = frozenset(Spectrum)
    SpectrumDic = {}
    score = 0
    for mass in IdealSet:
        IdealDic[mass] = IdealSpectrum.count(mass)
    for massy in SpectrumSet:
        SpectrumDic[massy] = Spectrum.count(massy)

    for mass in IdealDic.keys():
        if mass in SpectrumDic.keys():
            Idealvalue = IdealDic[mass]
            value = SpectrumDic[mass]
            minimum = min(Idealvalue, value)
            score = score + minimum
    return score


def LinearScore(Peptide, Spectrum):
    IdealSpectrum = LinearSpectrum(Peptide, Alphabet, AminoAcidMass)
    IdealSet = frozenset(IdealSpectrum)
    IdealDic = {}
    SpectrumSet = frozenset(Spectrum)
    SpectrumDic = {}
    score = 0
    for mass in IdealSet:
        IdealDic[mass] = IdealSpectrum.count(mass)
    for massy in SpectrumSet:
        SpectrumDic[massy] = Spectrum.count(massy)

    for mass in IdealDic.keys():
        if mass in SpectrumDic.keys():
            Idealvalue = IdealDic[mass]
            value = SpectrumDic[mass]
            minimum = min(Idealvalue, value)
            score = score + minimum
    return score


print(Score(Peptide, Spectrumy))
print(LinearScore(Peptide, Spectrumy))
