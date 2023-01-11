# String Composition Problem

k = int(input('Enter k: '))
Text = input('Enter Text: ')


def Composition(k, Text):
    # returns a kmer composing Text in lexicographic order

    KmerList = []
    n = len(Text)
    for i in range(n-k+1):
        window = Text[i:i+k]
        KmerList.append(window)
    KmerList.sort()
    return KmerList

for l in Composition(k, Text):
    print(l)


