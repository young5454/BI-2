# Peptide Encoding Problem

Pattern = open('dataset_96_7.txt').read()
peptide = "FKLGSMQQMY"

Codon_Dic = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

def DNAtoRNA(Pattern):
    # change T into U
    RNA = ''
    for nucleotide in Pattern:
        if nucleotide == 'T':
            RNA = RNA + 'U'
        else:
            RNA = RNA + nucleotide
    return RNA


def Composition(k, Text):
    # returns a kmer composing Text in lexicographic order

    KmerList = []
    n = len(Text)
    for i in range(n-k+1):
        window = Text[i:i+k]
        KmerList.append(window)
    KmerList.sort()
    return KmerList


def RevComp(Pattern):
    list = []
    for base in Pattern:
        if base == 'A':
            list.append('T')
        elif base == 'G':
            list.append('C')
        elif base == 'C':
            list.append('G')
        elif base == 'T':
            list.append('A')
    ReverseList = list[::-1]
    patternRC = ''
    for b in ReverseList:
        patternRC = patternRC + b
    return patternRC


def ProteinTranslation(Pattern):
    peptide = ''
    n = len(Pattern)
    k = int(n/3)
    i = 0
    while i < n:
        codon = Pattern[i:i+3]
        if codon in Codon_Dic.keys():
            if Codon_Dic[codon] != "STOP":
                peptide = peptide + Codon_Dic[codon]
            elif Codon_Dic[codon] == "STOP":
                break
        i = i + 3
    return peptide


def PepEncoding(Pattern, peptide):
    #Pattern_prime = RevComp(Pattern)
    #Pattern_rna_prime = DNAtoRNA(Pattern_prime)
    #Pattern_rna = DNAtoRNA(Pattern)

    pattern_list = []
    pep_len = len(peptide)
    k = pep_len * 3

    # generate all kmers from Pattern_rna and Pattern_rna'

    kmerlist = Composition(k, Pattern)

    for kmer in kmerlist:
        # not complementary
        kmer_U = DNAtoRNA(kmer)
        pep = ProteinTranslation(kmer_U)
        if pep == peptide:
            pattern_list.append(kmer)

    for kmer in kmerlist:
        # complementary
        kmer_comp = RevComp(kmer)
        kmer_comp_U = DNAtoRNA(kmer_comp)
        pep = ProteinTranslation(kmer_comp_U)
        if pep == peptide:
            pattern_list.append(kmer)
    return pattern_list


for item in PepEncoding(Pattern, peptide):
    print(item)

