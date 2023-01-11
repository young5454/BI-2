# Cyclopeptide Sequencing

Alphabet = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N',
            'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']

AminoAcidMass = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97,
    'V': 99, 'T': 101, 'C': 103, 'I': 113,
    'L': 113, 'N': 114, 'D': 115, 'K': 128,
    'Q': 128, 'E': 129, 'M': 131, 'H': 137,
    'F': 147, 'R': 156, 'Y': 163, 'W': 186}

#spectrum = [0, 113, 128, 186, 241, 299, 314, 427]

with open('dataset_100_6.txt') as file:
	for line in file:
		spectrum = map(int,line.split())

spectrum = list(set(spectrum))


def Expand(lists, spectrum):
    aa_weights = sorted(list(set(AminoAcidMass.values())))
    if lists == []:
        for weight in aa_weights:
            if weight in spectrum:
                lists.append([weight])
        return lists
    else:
        newlists = []
        for sublist in lists:
            newlist = []
            for weight in aa_weights:
                if (sum(sublist) + weight) in spectrum:
                    newlist.append(sublist + [weight])
            for x in newlist:
                newlists.append(x)
    return newlists


def CycloPeptideSequencing(spectrum):
    peptide = Expand([], spectrum)
    while sum(peptide[0]) != max(spectrum):
        peptide = Expand(peptide, spectrum)
    for res in sorted(peptide,reverse = True):
        print('-'.join(str(num) for num in res))


def CycloPeptideSequencingOutput(sequencing):
    output = ''
    for y in sequencing:
        list_string = map(str, y)
        joined_str = "-".join(list_string)
        print(joined_str)


print(Expand([], spectrum))
CycloPeptideSequencing(spectrum)
