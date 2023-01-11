# Implement Trim

import operator
from copy import deepcopy

#___________________________________________________

Leaderboard = ['LCEDSMPINATMDGTTWRGSTQMNTVLRHAESQCKKEFISI',
               'HFACYQFAAFCIYAGEYKMVGYIVCQVGTTGKRLNKALWER',
               'WRPWGEHGPAWKQCWRMPERMAYWIDDKEVRAGAHLQAVIW',
               'IPLGDGVYAGVRGWHLAPVEYCFLEFAIMMGAMEQSHMSTL',
               'VKITDANMMLETMMVSPNNFFLQSFECAVRTCLDPKIARSL',
               'PFVMWLGKMGVRSHMDLCSICSEFVYNDLYGGVWVVSDQSI',
               'VIIGTDLDDVSSRNLNHGYHNIHTWDMMLCMGPKHDVANNP',
               'EFAPHGAMSIKGPHDCQKAMHYCMWREFCIPQRLTYVAKGV',
               'YDNTLYQDQYGDVWACMVSDYWNYELTQLSHATDNELLYIQ',
               'MRAKYQWTFDQNGGRFKMTQKEFCAYRMKRITWDMRWCYNY',
               'DTHPGFFTVYPYAWCYIHGHFQHKPLCKEWLQPWCPKGHYW',
               'FEPKGSSMACGTYWMVQYHDYKNGNQFDRIFSFAQDRSKCT',
               'LISCGHQSDWYCEDTLLDQLIFHFGGNEFAGPKRKHCNDYI',
               'WVHIAFSSGMMMTHQEFVNNSLHYSDIRYVPQAEYMAMQRV',
               'GNRELNMGFMVNKSLAFFEIMKYYNNRHSWLKTVDDLTRKA',
               'AQSCMVQVRPSYYQYRGIWVSSHLNDQDFEIANPTKTKIEL',
               'NTMTHAQWWIQMHHEDCETNWLEADWFYGYQKQHEFGPTVH',
               'LWIYKIGEDWNREDNAELHDHYAHEKTRSNELHGFETLHKS']
N = 6
Spectrum = []
with open('dataset_4913_3.txt') as file:
    for line in file:
        Spectrum += line.rstrip().split()
    Spectrum = [int(x) for x in Spectrum]

Alphabet = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N',
            'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']

AminoAcidMass = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97,
    'V': 99, 'T': 101, 'C': 103, 'I': 113,
    'L': 113, 'N': 114, 'D': 115, 'K': 128,
    'Q': 128, 'E': 129, 'M': 131, 'H': 137,
    'F': 147, 'R': 156, 'Y': 163, 'W': 186}
#____________________________________________________

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


def Trim(Leaderboard, Spectrum, N, Alphabet, AminoAcidMass):
    LeaderDic = {}
    for peptide in Leaderboard:
        score = LinearScore(peptide, Spectrum)
        LeaderDic[peptide] = score
    SortedLeaderDic = dict(sorted(LeaderDic.items(), key=operator.itemgetter(1), reverse=True))
    copy = deepcopy(SortedLeaderDic)
    values = list(SortedLeaderDic.values())
    cut = values[N-1]
    for key in SortedLeaderDic.keys():
        if SortedLeaderDic[key] < cut:
            del copy[key]
    trimmedleaderboard = list(copy.keys())
    return trimmedleaderboard


for item in Trim(Leaderboard, Spectrum, N, Alphabet, AminoAcidMass):
    print(item)

