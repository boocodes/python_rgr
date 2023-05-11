

class Genethic_algorithm:

    def dikstryFitness(individual):
        startV = 0
        s = 1
        for n, path in enumerate(individual):
            path = path[:path.index(n)+1]

            si = startV
            for j in path:
                s += D[si][j]
                si = j

        return s,         # кортеж
    def cxOrdered(ind1, ind2):
        for p1, p2 in zip(ind1, ind2):
            tools.cxOrdered(p1, p2)

        return ind1, ind2
    def mutShuffleIndexes(individual, indpb):
        for ind in individual:
            tools.mutShuffleIndexes(ind, indpb)

        return individual,