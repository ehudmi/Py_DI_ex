# Instructions :
# This challenge is about Biology that will put emphasis on your knowledge of classes, inheritance and polymorphism.

# Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.
# A Gene is a single value 0 or 1, it can mutate (flip).
# A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip
# (1/2 chance to flip).
# A DNA is a series of 10 chromosomes, and it can also mutate the same way Chromosomes can mutate.

# Implement these classes as you see fit.

# Create a new class called Organism that accepts a DNA object and an environment parameter that sets the
# probability for its DNA to mutate.

# Instantiate a number of Organism and let them mutate until one gets to a DNA which is only made of 1s.
# Then stop and record the number of generations (iterations) it took.
# Write your results in you personal biology research notebook and tell us your conclusion :).
from random import randint
from random import choices


class Gene:
    def __init__(self, num=randint(0, 1)):
        self.state = num

    def flip(self):
        if self.state == 0:
            self.state = 1
        else:
            self.state = 0


class Chromosome(Gene):
    def __init__(self, gene_list, num=randint(0, 1)):
        super().__init__(num)
        self.gene_list = gene_list

    def chr_flip(self):
        self.gene_num = randint(0, 10)
        # self.gene_list = map()
