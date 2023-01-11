# Overlap Graph Problem

Patternsy = ["ATGCG",
"GCATG",
"CATGC",
"AGGCA",
"GGCAT",
"GGCAC"]
Patterns = ["0000",
            "0001", "0010", "0100", "1000",
            "0011", "0101", "1001", "0110", "1010", "1100",
            "1110", "1101", "1011", "0111",
            "1111"]
Patternr = ["AAG",
"AGA",
"ATT",
"CTA",
"CTC",
"GAT",
"TAA",
"TCT",
"TTC",
"AGA"]

def Prefix(Pattern):
    k = len(Pattern)
    return Pattern[0:k-1]

def Suffix(Pattern):
    k = len(Pattern)
    return Pattern[1:k]


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def Overlap(Patterns):
    dic = {}
    n = len(Patterns)
    for i in range(n):
        suffix = Suffix(Patterns[i])
        pattern_list = []
        for pattern in Patterns:
            if Prefix(pattern) == suffix:
                pattern_list.append(pattern)
                dic[Patterns[i]] = pattern_list
    for keys in dic.keys():
        joined_string = ",".join(dic[keys])
        print(keys + " -> " + joined_string)


Overlap(Patternr)

