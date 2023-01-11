# String Spelled by a Genome Path Problem

path = open('dataset_198_3.txt').read().split()

def PathToGenome(path):
    # path is a list

    FirstSequence = path[0]
    n = len(path)
    k = len(FirstSequence)
    for i in range(1,n):
        FirstSequence = FirstSequence + path[i][k-1]
    return FirstSequence

print(PathToGenome(path))

