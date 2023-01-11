# The Cyclopeptide Sequencing Problem

n = int(input('Enter n: '))

def CyclicSubpepcount(n):
    sum = 0
    for i in range(n):
        sum = sum + i
    return sum*2

print(CyclicSubpepcount(n))


def LinearSubpepCount(n):
    sum = 0
    for i in range(n+1):
        sum = sum + i
    return sum+1


print(LinearSubpepCount(n))

